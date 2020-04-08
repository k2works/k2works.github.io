
UML
==================
ユースケース図
------------------

.. uml::

   left to right direction
   skinparam packageStyle rectangle
   actor customer
   actor clerk
   rectangle checkout {
     customer -- (checkout)
     (checkout) .> (payment) : include
     (help) .> (checkout) : extends
     (checkout) -- clerk
   }


クラス図
------------------

.. uml::

   class Car
   Driver - Car : drives >
   Car *- Wheel : have 4 >
   Car -- Person : < owns


シーケンス図
------------------

.. uml::

   participant User
   User -> A: DoWork
   activate A
   A -> B: << createRequest >>
   activate B
   B -> C: DoWork
   activate C
   C --> B: WorkDone
   destroy C
   B --> A: RequestCreated
   deactivate B
   A -> User: Done
   deactivate A
