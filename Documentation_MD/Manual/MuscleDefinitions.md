[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/MuscleDefinitions.html)
  * [中文](/cn/current/Manual/MuscleDefinitions.html)
  * [日本語](/ja/current/Manual/MuscleDefinitions.html)
  * [한국어](/kr/current/Manual/MuscleDefinitions.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/MuscleDefinitions.html)
  * [中文](/cn/current/Manual/MuscleDefinitions.html)
  * [日本語](/ja/current/Manual/MuscleDefinitions.html)
  * [한국어](/kr/current/Manual/MuscleDefinitions.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Models](models.html)
  * [Importing models into Unity](models-importing.html)
  * [Model Import Settings window](class-FBXImporter.html)
  * [Rig tab](FBXImporter-Rig.html)
  * Avatar Muscle & Settings tab

[](class-Avatar.html)

Avatar Mapping tab

[](class-AvatarMask.html)

Avatar Mask window

# Avatar Muscle & Settings tab

Unity’s animation system allows you to control the range of motion of
different bones using **Muscles**.

Once the Avatar has been [properly configured](class-Avatar.html), the
animation system “understands” the bone structure and allows you to start
using the **Muscles & Settings** tab of the **Avatar** An interface for
retargeting animation from one rig to another. [More
info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar)’s **Inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector). Use the **Muscles & Settings** tab
to tweak the character’s range of motion and ensure the character deforms in a
convincing way, free from visual artifacts or self-overlaps.

![The Muscles &amp; Settings tab in the Avatar
window](../uploads/Main/MecanimAvatarMuscles.png) The **Muscles & Settings**
tab in the **Avatar** window

The areas of the **Muscle & Settings** tab include:

**(A)** Buttons to toggle between the **Mapping** and **Muscles & Settings**
tabs. You must **Apply** or **Revert** any changes made before switching
between tabs.

**(B)** Use the **Muscle Group Preview** area to manipulate the character
using predefined deformations. These affect several bones at once.

**(C)** Use the **Per-Muscle Settings** area to adjust individual bones in the
body. You can expand the muscle settings to change the range limits of each
settings. For example, by default, Unity gives the Head-Nod and Head-Tilt
settings a possible range of –40 to 40 degrees but you can decrease these
ranges even further to add stiffness to these movements.

**(D)** Use the **Additional Settings** to adjust specific effects in the
body.

**(E)** The **Muscles** menu provides a **Reset** tool to return all muscle
settings to their default values.

**(F)** Buttons to accept any changes made (**Accept**), discard any changes
(**Revert**), and leave the Avatar window (**Done**). You must **Apply** or
**Revert** any changes made before leaving the **Avatar** window.

## Previewing changes

For the settings in the **Muscle Group Preview** and **Per-Muscle Settings**
areas, you can preview the changes right in the **Scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view. You can drag the sliders left and
right to see the range of movement for each setting applied to your character:

![Preview the changes to the muscles settings in the Scene
view](../uploads/Main/MuscleDefinitions-SceneView.png) Preview the changes to
the muscles settings in the Scene view

You can see the bones of the skeleton through the **Mesh** The main graphics
primitive of Unity. Meshes make up a large part of your 3D worlds. Unity
supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv
surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh).

## Translate Degree of Freedom (DoF)

You can enable the **Translate DoF** The three degrees-of-freedom associated
with translation (movement in X,Y & Z) as opposed to rotation.  
See in [Glossary](Glossary.html#TranslateDoF) option in the **Additional
Settings** to enable translation animations for the humanoid. If this option
is disabled, Unity animates the bones using only rotations. **Translation
DoF** is available for Chest, UpperChest, Neck, LeftUpperLeg, RightUpperLeg,
LeftShoulder and RightShoulder muscles.

**Note:** Enabling **Translate DoF** can increase performance requirements,
because the animation system needs to perform an extra step to retarget
**humanoid animation** An animation using humanoid skeletons. Humanoid models
generally have the same basic structure, representing the major articulate
parts of the body, head and limbs. This makes it easy to map animations from
one humanoid skeleton to another, allowing retargeting and inverse kinematics.
[More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Humanoidanimation). For this reason, you
should only enable this option if you know your animation contains animated
translations of some of the bones in your character.

[](class-Avatar.html)

Avatar Mapping tab

[](class-AvatarMask.html)

Avatar Mask window

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

