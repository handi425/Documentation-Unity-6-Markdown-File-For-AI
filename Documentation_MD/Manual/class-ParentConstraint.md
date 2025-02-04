[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-ParentConstraint.html)
  * [中文](/cn/current/Manual/class-ParentConstraint.html)
  * [日本語](/ja/current/Manual/class-ParentConstraint.html)
  * [한국어](/kr/current/Manual/class-ParentConstraint.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-ParentConstraint.html)
  * [中文](/cn/current/Manual/class-ParentConstraint.html)
  * [日本語](/ja/current/Manual/class-ParentConstraint.html)
  * [한국어](/kr/current/Manual/class-ParentConstraint.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Constraints](Constraints.html)
  * Parent Constraints 

[](class-LookAtConstraint.html)

Look At Constraints

[](class-PositionConstraint.html)

Position Constraints

# Parent Constraints

A Parent Constraint moves and rotates a **GameObject** The fundamental object
in Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) as if it is the child of another
GameObject in the Hierarchy window. However, it offers certain advantages that
are not possible when you make one GameObject the parent of another:

  * A Parent Constraint does not affect scale. 

  * A Parent Constraint can link to multiple GameObjects.

  * A GameObject does not have to be a child of the GameObjects that the Parent Constraint links to.

  * You can vary the effect of the Constraint by specifying a weight, as well as weights for each of its source GameObjects.

For example, to place a sword in the hand of a character, add a Parent
Constraint component to the sword GameObject. In the **Sources** list of the
Parent Constraint, link to the character’s hand. This way, the movement of the
sword is constrained to the position and rotation of the hand.

![Parent Constraint component](../uploads/Main/ParentConstraint.png) Parent
Constraint component

### Properties

**Property:** | **Function:**  
---|---  
**Activate** | After you move and rotate the constrained GameObject and its source GameObjects, click **Activate** to save this information. **Activate** saves the current offset from the source GameObjects in **Rotation At Rest** , **Position At Rest** , **Position Offset** , and **Rotation Offset** , then checks **Is Active** and **Lock**.  
**Zero** | Sets the position and rotation of the constrained GameObject to the source GameObjects. **Zero** resets the **Rotation At Rest** , **Position At Rest** , **Position Offset** , and **Rotation Offset** fields then checks **Is Active** and **Lock**.  
**Is Active** | Toggles whether or not to evaluate the Constraint. To also apply the Constraint, make sure **Lock** is checked.  
**Weight** | The strength of the Constraint. A weight of 1 causes the Constraint to move and rotate this GameObject at the same rate as its source GameObjects. A weight of 0 removes the effect of the Constraint completely. This weight affects all source GameObjects. Each GameObject in the **Sources** list also has a weight.  
**Constraint Settings** |   
| Lock | Toggle to let the Constraint move and rotate the GameObject. Uncheck this property to edit the position and rotation of this GameObject. You can also edit the Rotation At Rest, Position At Rest, Position Offset, and Rotation Offset properties. If Is Active is checked, the Constraint updates the Rotation At Rest, Position At Rest, Position Offset, or Rotation Offset properties for you as you move and rotate the GameObject or its Source GameObjects. When you are satisfied with your changes, check Lock to let the Constraint to control this GameObject. This property has no effect in Play Mode.  
| Position At Rest | The X, Y, and Z values to use when Weight is 0 or when the corresponding **Freeze Position Axes** are not checked. To edit these fields, uncheck **Lock**.  
| Rotation At Rest | The X, Y, and Z values to use when Weight is 0 or when the corresponding **Freeze Rotation Axes** are not checked. To edit these fields, uncheck **Lock**.  
| Position Offset | The X, Y, and Z position offset from the Transform that the Constraint imposes. To edit these fields, uncheck **Lock**.  
| Rotation Offset | The X, Y, and Z rotation offset from the Transform that the Constraint imposes. To edit these fields, uncheck **Lock**.  
| Freeze Position Axes | Check X, Y, or Z to allow the Constraint to control the corresponding position axes. Uncheck an axis to stop the Constraint from controlling it, which allows you to edit, animate, or script it.  
| Freeze Rotation Axes | Check X, Y, or Z to allow the Constraint to control the corresponding rotation axes. Uncheck an axis to stop the Constraint from controlling it, which allows you to edit, animate, or script it.  
**Sources** | The list of GameObjects that constrain this GameObject. Unity evaluates source GameObjects in the order they appear in this list. This order affects how this Constraint moves and rotates the constrained GameObject. To get the result you want, drag and drop items in this list. Each source has a weight from 0 to 1.  
  
* * *

  * 2018–03–13 Page published 

  * Constraints added in 2018.1

ParentConstraint

[](class-LookAtConstraint.html)

Look At Constraints

[](class-PositionConstraint.html)

Position Constraints

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

