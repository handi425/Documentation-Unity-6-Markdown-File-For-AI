[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-ScaleConstraint.html)
  * [中文](/cn/current/Manual/class-ScaleConstraint.html)
  * [日本語](/ja/current/Manual/class-ScaleConstraint.html)
  * [한국어](/kr/current/Manual/class-ScaleConstraint.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-ScaleConstraint.html)
  * [中文](/cn/current/Manual/class-ScaleConstraint.html)
  * [日本語](/ja/current/Manual/class-ScaleConstraint.html)
  * [한국어](/kr/current/Manual/class-ScaleConstraint.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Constraints](Constraints.html)
  * Scale Constraints

[](class-RotationConstraint.html)

Rotation Constraints

[](working-with-scenes.html)

Working with scenes

# Scale Constraints

A Scale Constraint component resizes a **GameObject** The fundamental object
in Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to match the scale of its source
GameObjects.

![Scale Constraint component](../uploads/Main/ScaleConstraint.png) Scale
Constraint component

### Properties

**Property:** | **Function:**  
---|---  
**Activate** | After you resize the constrained GameObject and its source GameObjects, click **Activate** to save this information. **Activate** saves the current offset from the source GameObjects in **Scale At Rest** and **Scale Offset** then checks **Is Active** and **Lock**.  
**Zero** | Sets the rotation of the constrained GameObject to the source GameObjects. **Zero** resets the **Scale At Rest** and **Scale Offset** fields then checks **Is Active** and **Lock**.  
**Is Active** | Toggles whether or not to evaluate the Constraint. To also apply the Constraint, make sure **Lock** is checked.  
**Weight** | The strength of the Constraint. A weight of 1 causes the Constraint to resize this GameObject at the same rate as its source GameObjects. A weight of 0 removes the effect of the Constraint completely. This weight affects all source GameObjects. Each GameObject in the **Sources** list also has a weight.  
**Constraint Settings** |   
| Lock | Toggle to let the Constraint resize the GameObject. Uncheck this property to edit the scale of this GameObject. You can also edit the **Scale At Rest** and **Scale Offset** properties. If **Is Active** is checked, the Constraint updates the **Scale At Rest** or **Scale Offset** properties for you as you resize the GameObject or its Source GameObjects. When you are satisfied with your changes, check **Lock** to let the Constraint to control this GameObject. This property has no effect in Play Mode.  
| Scale At Rest | The X, Y, and Z values to use when **Weight** is 0 or when the corresponding **Freeze Scale Axes** is not checked. To edit these fields, uncheck **Lock**.  
| Scale Offset | The X, Y, and Z offset from the transform that is imposed by the Constraint. To edit these fields, uncheck Lock.  
| Freeze Scale Axes | Check X, Y, or Z to allow the Constraint to control the corresponding axes. Uncheck an axis to stop the Constraint from controlling it. This allows you to edit, animate, or script the unfrozen axis.  
**Sources** | The list of GameObjects that constrain this GameObject. Each source has a weight from 0 to 1.  
  
* * *

  * 2018–03–13 Page published 

  * Constraints added in 2018.1

ScaleConstraint

[](class-RotationConstraint.html)

Rotation Constraints

[](working-with-scenes.html)

Working with scenes

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

