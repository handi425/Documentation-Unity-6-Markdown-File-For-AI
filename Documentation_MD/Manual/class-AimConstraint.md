[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-AimConstraint.html)
  * [中文](/cn/current/Manual/class-AimConstraint.html)
  * [日本語](/ja/current/Manual/class-AimConstraint.html)
  * [한국어](/kr/current/Manual/class-AimConstraint.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-AimConstraint.html)
  * [中文](/cn/current/Manual/class-AimConstraint.html)
  * [日本語](/ja/current/Manual/class-AimConstraint.html)
  * [한국어](/kr/current/Manual/class-AimConstraint.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Constraints](Constraints.html)
  * Aim Constraints

[](Constraints.html)

Constraints

[](class-LookAtConstraint.html)

Look At Constraints

# Aim Constraints

An Aim Constraint rotates a **GameObject** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to face its source GameObjects. It
can also maintain a consistent orientation for another axis. For example, you
can add an Aim Constraint to a **Camera** A component which creates an image
of a particular viewpoint in your scene. The output is either drawn to the
screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). To keep the Camera upright while the
Constraint aims it, specify the up axis of the Camera and an up direction to
align it to.

Use the **Up Vector** to specify the up axis of a constrained GameObject. Use
the **World Up Vector** to specify the upward direction. As the Aim Constraint
rotates the GameObject to face its source GameObjects, the Constraint also
aligns the up axis of the constrained GameObject with the upward direction.

![Aim Constraint component](../uploads/Main/AimConstraint.png) Aim Constraint
component

### Properties

**Property:** | **Function:**  
---|---  
**Activate** | After you rotate the constrained GameObject and move its source GameObjects, click **Activate** to save this information. **Activate** saves the current offset from the source GameObjects in **Rotation At Rest** and **Rotation Offset** , then checks **Is Active** and **Lock**.  
**Zero** | Sets the rotation of the constrained GameObject to the source GameObjects. Zero resets the **Rotation At Rest** and **Rotation Offset** fields, then checks **Is Active** and **Lock**.  
**Is Active** | Toggles whether or not to evaluate the Constraint. To also apply the Constraint, make sure **Lock** is checked.  
**Weight** | The strength of the Constraint. A weight of 1 causes the Constraint to rotate the GameObject at the same rate that its source GameObjects move. A weight of 0 removes the effect of the Constraint completely. This weight affects all source GameObjects. Each GameObject in the **Sources** list also has a weight.  
**Aim Vector** | Specifies the axis which faces the direction of its source GameObjects. For example, to specify that the GameObject should orient only its positive Z axis to face the source GameObjects, enter an **Aim Vector** of 0, 0, 1 for the X, Y, and Z axes, respectively.  
**Up Vector** | Specifies the up axis of this GameObject. For example, to specify that the GameObject should always keep its positive Y axis pointing upward, enter an **Up Vector** of 0, 1, 0 for the X, Y, and Z axes, respectively.  
**World Up Type** | Specifies the axis for the upward direction. The Aim Constraint uses this vector to align the up axis of the GameObject the upward direction.  
| **Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) Up | The Y axis of the scene.  
| Object Up | The Y axis of the GameObject referred to by **World Up Object**.  
| Object Up Rotation | The axis specified by **World Up Vector** of the GameObject referred to by **World Up Object**.  
| Vector | The World Up Vector.  
| None | Do not use a World Up vector.  
**World Up Vector** | Specifies the vector to use for the **Object Up Rotation** and **Vector** choices in **World Up Type**.  
**World Up Object** | Specifies the GameObject to use for the **Object Up** and **Object Up Rotation** choices in **World Up Type**.  
**Constraint Settings** |   
| Lock | Enable this setting to let the Constraint rotate the GameObject. Uncheck this property to edit the rotation of this GameObject. You can also edit the Rotation At Rest and Rotation Offset properties. If Is Active is checked, the Constraint updates the Rotation At Rest or Rotation Offset properties for you as you rotate the GameObject or its source GameObjects. When you are satisfied with your changes, check Lock to let the Constraint control this GameObject. This property has no effect in Play Mode.  
| Rotation At Rest | The X, Y, and Z values to use when Weight is 0 or when the corresponding Freeze Rotation Axes are not checked. To edit these fields, uncheck Lock.  
| Rotation Offset | The X, Y, and Z offset from the rotation that is calculated by the Constraint. To edit these fields, uncheck Lock.  
| Freeze Rotation Axes | Check X, Y, or Z to allow the Constraint to control the corresponding axes. Uncheck an axis to stop the Constraint from controlling it. This allows you to edit, animate, or script the unfrozen axis.  
**Sources** | The list of GameObjects that constrain this GameObject. Unity evaluates source GameObjects in the order that they appear in this list. This order affects how this Constraint rotates the constrained GameObject. To get the result you want, drag and drop items in this list. Each source has a weight from 0 to 1.  
  
AimConstraint

[](Constraints.html)

Constraints

[](class-LookAtConstraint.html)

Look At Constraints

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

