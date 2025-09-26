=========
Validator
=========


Functions
=========

Spec::If
--------

:Description: Evaluates a condition and returns the value of either the true or false case.
:Format: ``Spec::If: [ condition, true-value, false-value ]``

.. code-block:: yaml
    :caption: Example usage of Spec::If

    ListenerRule:
      _KeyRegex: ".*ListenerRule"
      _KeyCardinality:
        Spec::If:
          - Spec::Property: [ ApplicationLoadBalancer ]
          - 0-20
          - 0

In the above example, _KeyCardinality will be 0-20 if the ApplicationLoadBalancer key exists, otherwise it will be 0.

Spec::Property
--------------

:Description: Returns true if a property exists or has a particular value
:Format: ``Spec::Property: [ key(, value) ]``

.. code-block:: yaml
    :caption: Check if 'ApplicationLoadBalancer' exists using Spec::Property

    TargetGroup:
      _Required:
        Spec::Property: [ ApplicationLoadBalancer ]

.. code-block:: yaml
    :caption: Check if VolumeType has value 'io1' using Spec::Property

    Iops:
      _Type: int
      _Required:
        Spec::Property: [ VolumeType, io1 ]
      _Configurable:
        Spec::Property: [ VolumeType, io1 ]

Spec::Not
---------

:Description: Invert a condition
:Format: ``Spec::Not: condition``

.. code-block:: yaml
    :caption: Invert a Spec::Property condition using Spec::Not

    Cooldown:
      _Type: int
      _Required: false
      _Configurable:
        Spec::Not:
          Spec::Property: [ PolicyType, StepScaling ]

Spec::Or
--------

:Description: Logical 'or' multiple conditions
:Format: ``Spec::Or: [ condition(, condition)* ]``

.. code-block:: yaml
    :caption: Spec::Or example

    ScalingAdjustment:
      _Type: int
      _Required:
        Spec::Or:
          - Spec::Property: [ PolicyType, SimpleScaling ]
          - Spec::Not:
              Spec::Property: [ PolicyType ]

Spec::And
---------

:Description: Logical 'and' multiple conditions
:Format: ``Spec::And: [ condition(, condition)* ]``

.. code-block:: yaml
    :caption: Spec::And example

    StepName:
      _Type: int
      _Configurable:
        Spec::And:
          - Spec::Property: [ PolicyType, SimpleScaling ]
          - Spec::Property: [ CookieName ]
