[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AnimationRootMotionNodeOnImportedClips.html)
  * [中文](/cn/current/Manual/AnimationRootMotionNodeOnImportedClips.html)
  * [日本語](/ja/current/Manual/AnimationRootMotionNodeOnImportedClips.html)
  * [한국어](/kr/current/Manual/AnimationRootMotionNodeOnImportedClips.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AnimationRootMotionNodeOnImportedClips.html)
  * [中文](/cn/current/Manual/AnimationRootMotionNodeOnImportedClips.html)
  * [日本語](/ja/current/Manual/AnimationRootMotionNodeOnImportedClips.html)
  * [한국어](/kr/current/Manual/AnimationRootMotionNodeOnImportedClips.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Models](models.html)
  * [Importing models into Unity](models-importing.html)
  * [Model Import Settings window](class-FBXImporter.html)
  * [Animation tab](class-AnimationClip.html)
  * Motion

[](AnimationMaskOnImportedClips.html)

Mask

[](FBXImporter-Materials.html)

Materials tab

# Motion

Unity uses **root motion** Motion of character’s root node, whether it’s
controlled by the animation itself or externally. [More info](RootMotion.html)  
See in [Glossary](Glossary.html#RootMotion) to displace and orient the
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) at the root of the Animator
hierarchy for all **Animation clips** Animation data that can be used for
animated characters or simple animations. It is a simple “unit” piece of
motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More
info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip). Sometimes, it is necessary to
select a different node to act as the root motion source rather than the
designated node.

To select a different Root Motion Node for all animation clips:

  1. Expand the Motion section.

  2. Select the new root motion source from the Root Motion Node menu. This menu list all the objects and nodes under the root of the imported file’s hierarchy. This includes _None_ (designated node) and _**Root Transform** The Transform at the top of a hierarchy of Transforms. In a Prefab, the Root Transform is the topmost Transform in the Prefab. In an animated humanoid character, the Root Transform is a projection on the Y plane of the Body Transform and is computed at run time. At every frame, a change in the Root Transform is computed, and then this is applied to the GameObject to make it move. [More info](RootMotion.html)  
See in [Glossary](Glossary.html#RootTransform)_, your character’s **mesh** The
main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) objects, the root bone name, and a
submenu for each item with child objects. Each submenu also contains the child
object(s) themself and further sub-menus if those objects have child objects.

  3. Select Apply.

![Traverse the hierarchy of objects to select a root motion
node](../uploads/Main/AnimationInspectorRootNodeSelectionMenu.png) Traverse
the hierarchy of objects to select a root motion node

When you select a different Root Motion Node, the newly selected root motion
source overrides the manual root motion settings for each imported animation
clip. This hides and overriddes the Root Transform Rotation, Root Transform
Position (Y), and Root Transform Position (XZ) settings.

[](AnimationMaskOnImportedClips.html)

Mask

[](FBXImporter-Materials.html)

Materials tab

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

