========================================
Useful patterns to accelerate onboarding
========================================

Context
=======

As applications become more complex, we have dependencies between components.  We may need to reference outputs from other components, such as DNS names and connection strings.

By using the **DependsOn** property, the dependent component is given the context of the stack it is dependent on.  The context is available in S3 and can be pulled down using the files section in cfn-init.

We can export the context and make it available to the instance through environment variables by executing context.sh in the commands section of cfn-init.

Now that the context variables are made into environment variables on the system, we can write other scripts to make use of the variables.


sed
---

We can use a tool like sed to find a replace strings.

For example, we may need to update the standalone.xml on an EC2 instance with the RDS connection string for a JBoss application.

Sample snippet of datasource tag in standalone.xml for JBoss:

.. code-block:: xml
    :linenos:

    <datasources>
       <datasource jndi-name="java:jboss/datasources/MySqlDS" pool-name="MySqlDS">
          <connection-url>jdbc:mysql://localhost:3306/EJB3</connection-url>
             <driver>com.mysql</driver>
          <transaction-isolation>TRANSACTION_READ_COMMITTED</transaction-isolation>
          <pool>
            <min-pool-size>10</min-pool-size>
            <max-pool-size>100</max-pool-size>
            <prefill>true</prefill>
          </pool>
          <security>
            <user-name>test</user-name>
            <password>test</password>
          </security>
          <statement>
            <prepared-statement-cache-size>32</prepared-statement-cache-size>
            <share-prepared-statements/>
          </statement>
        </datasource>
        <drivers>
          <driver name="com.mysql" module="com.mysql">
            <xa-datasource-class>com.mysql.jdbc.jdbc2.optional.MysqlXADataSource</xa-datasource-class>
          </driver>
        </drivers>
    </datasources>

We first need to generalize the configuration file so it can be used in all environments.  We can do this by replacing the <connection-url>, <user-name>, and <password> values with a unique string we can find and replace on:

.. code-block:: xml
    :linenos:

    <datasources>
       <datasource jndi-name="java:jboss/datasources/MySqlDS" pool-name="MySqlDS">
          <connection-url>{{ vars.context.connection-url }}</connection-url>
             <driver>com.mysql</driver>
          <transaction-isolation>TRANSACTION_READ_COMMITTED</transaction-isolation>
          <pool>
            <min-pool-size>10</min-pool-size>
            <max-pool-size>100</max-pool-size>
            <prefill>true</prefill>
          </pool>
          <security>
            <user-name>{{ vars.user-name }}</user-name>
            <password>{{ vars.password }}</password>
          </security>
          <statement>
            <prepared-statement-cache-size>32</prepared-statement-cache-size>
            <share-prepared-statements/>
          </statement>
        </datasource>
        <drivers>
          <driver name="com.mysql" module="com.mysql">
            <xa-datasource-class>com.mysql.jdbc.jdbc2.optional.MysqlXADataSource</xa-datasource-class>
          </driver>
        </drivers>
    </datasources>

In the above example, we used {{ vars.<name of variable> }}.

We can now write a sed script to find and replace these values:

.. code-block:: shell
    :linenos:

    #!/bin/bash

    source /opt/pipeline/context.sh

    sed -i "s/{{ vars.context.connection-url }}/$rds_ConnectionUrl/g" /opt/jboss/jboss-6.4/config/standalone.xml
    sed -i "s/{{ vars.user-name }}/{{ vars.MasterUsername }}/g" /opt/jboss/jboss-6.4/config/standalone.xml
    # Not used anymore - master user password handled by RDS internally to the component.
    # sed -i "s/{{ vars.password }}/{{ vars.MasterUserPassword }}/g" /opt/jboss/jboss-6.4/config/standalone.xml

- Line 3 sources the ``context.sh`` script making ``$rds_ConnectionUrl`` available.
- Line 4 does a find and replace on ``{{ vars.context.connection-url }}`` with ``$rds_ConnectionUrl`` in the file ``/opt/jboss/jboss-6.4/config/standalone.xml``
- Line 5 and 6 does a find and replace on ``{{ vars.user-name }}`` and ``{{ vars.password }}`` with ``{{ vars.MasterUsername }}`` and ``{{ vars.MasterUserPassword }}``.
- ``{{ vars.MasterUsername }}`` and ``{{ vars.MasterUserPassword }}`` are taken from the ``vars.yaml`` in ``platform/vars``
