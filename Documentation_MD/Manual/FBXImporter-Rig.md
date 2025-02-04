[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/FBXImporter-Rig.html)
  * [中文](/cn/current/Manual/FBXImporter-Rig.html)
  * [日本語](/ja/current/Manual/FBXImporter-Rig.html)
  * [한국어](/kr/current/Manual/FBXImporter-Rig.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/FBXImporter-Rig.html)
  * [中文](/cn/current/Manual/FBXImporter-Rig.html)
  * [日本語](/ja/current/Manual/FBXImporter-Rig.html)
  * [한국어](/kr/current/Manual/FBXImporter-Rig.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Models](models.html)
  * [Importing models into Unity](models-importing.html)
  * [Model Import Settings window](class-FBXImporter.html)
  * Rig tab

[](FBXImporter-Model.html)

Model tab

[](class-Avatar.html)

Avatar Mapping tab

# Rig tab

The settings on the **Rig** tab define how Unity maps the deformers to the
**Mesh** The main graphics primitive of Unity. Meshes make up a large part of
your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes.
Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) in the imported Model so that you can
animate it. For Humanoid characters, this means [assigning or creating an
Avatar](ConfiguringtheAvatar.html). For non-Humanoid (_Generic_) characters,
this means [identifying a Root bone in the skeleton](GenericAnimations.html).

By default, when you select a Model in the **Project** In Unity, you use a
project to design and develop a game. A project stores all of the files that
are related to a game, such as the asset and Scene files. [More
info](2Dor3D.html)  
See in [Glossary](Glossary.html#Project) view, Unity determines which
**Animation Type** best matches the selected Model and displays it in the
**Rig** tab. If Unity has never imported the file, the Animation Type is set
to **None** :

![No rig mapping](../uploads/Main/Rig-0.png) No rig mapping **Property:** | **Function:**  
---|---  
**Animation Type** | Specfiy the type of animation.  
| **None** | No animation present  
| **Legacy** | Use the Legacy Animation System. Import and use animations as with Unity version 3.x and earlier.  
| **Generic** | Use the Generic Animation System if your rig is _non-humanoid_ (quadruped or any entity to be animated). Unity picks a root node but you can identify another bone to use as the **Root node** A transform in an animation hierarchy that allows Unity to establish consistency between Animation clips for a generic model. It also enables Unity to properly blend between Animations that have not been authored “in place” (that is, where the whole Model moves its world position while animating). [More info](AnimationRootMotionNodeOnImportedClips.html)  
See in [Glossary](Glossary.html#Rootnode) instead.  
| **Humanoid** | Use the Humanoid Animation System if your rig is _humanoid_ (it has two legs, two arms and a head). Unity usually detects the skeleton and maps it to the Avatar correctly. In some cases, you may need to set a change the **Avatar Definition** and **Configure** the mapping manually.  
  
## Generic animation types

![Your rig is non-humanoid \(quadruped or any entity to be
animated\)](../uploads/Main/Rig-1.png) Your rig is _non-humanoid_ (quadruped
or any entity to be animated)

[Generic Animations](GenericAnimations.html) do not use Avatars like
**Humanoid animations** An animation using humanoid skeletons. Humanoid models
generally have the same basic structure, representing the major articulate
parts of the body, head and limbs. This makes it easy to map animations from
one humanoid skeleton to another, allowing retargeting and inverse kinematics.
[More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Humanoidanimation) do. Since the skeleton can
be arbitrary, you must specify which bone is the **Root node**. The Root node
allows Unity to establish consistency between **Animation clips** Animation
data that can be used for animated characters or simple animations. It is a
simple “unit” piece of motion, such as (one specific instance of) “Idle”,
“Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) for a generic model, and blend
properly between Animations that have not been authored “in place” (that is,
where the whole model moves its world position while animating).

Specifying the root node helps Unity determine between movement of the bones
relative to each other, and motion of the Root node in the world (controlled
from [OnAnimatorMove](../ScriptReference/MonoBehaviour.OnAnimatorMove.html)).

**Property:** | **Function:**  
---|---  
**Avatar Definition** | Choose where to get the Avatar definition.  
| **Create from this model** | Create an Avatar based on this model  
| **Copy from Other Avatar** | Point to an Avatar set up on another model.  
**Root node** | Select the bone to use as a root node for this Avatar.   
  
This setting is only available if you set the **Avatar Definition** to
**Create From This Model**.  
**Source** | Copy another Avatar with an identical rig to import its animation clips.   
  
This setting is only available if you set the **Avatar Definition** to **Copy
from Other Avatar**.  
**Skin Weights** | Set the maximum number of bones that can influence a single vertex.  
  
  
| **Standard (4 Bones)** | Use a maximum influence of four bones. This is the default, and is recommended for performance.  
| **Custom** | Set your own maximum number of bones.   
  
When you select this option, the **Max Bones/Vertex** and **Max Bone Weight**
properties appear.  
**Max Bones/Vertex** | Set the maximum number of bones per vertex to influence a given vertex. You can set between 1 and 32 bones per vertex, but the higher the number of bones you use to influence a vertex, the greater the performance cost.  
  
This setting is only available you set the **Skin Weights** property to
**Custom**.  
**Max Bone Weight** | Set the bottom threshold for considering bone weights. The weighting calculation ignores anything smaller than this value, and Unity scales up the bone weights higher than this value to a total of 1.0.  
  
This setting is only available if the **Skin Weights** property is set to
**Custom**.  
**Optimize Game Object** | Remove and store the GameObject Transform hierarchy of the imported character in the Avatar and Animator component. If enabled, the SkinnedMeshRenderers of the character use the Unity animation system’s internal skeleton, which improves the performance of the animated characters.   
  
Only available if the **Avatar Definition** is set to **Create From This
Model**.  
**Extra Transforms to Expose** | Specify which Transform paths you want Unity to ignore when **Optimize Game Object** is enabled. For more information, see Including extra Transforms.  
  
This section only appears when **Optimize Game Object** is enabled.  
  
## Humanoid animation types

![Your rig is humanoid \(it has two legs, two arms and a
head\)](../uploads/Main/Rig-2.png) Your rig is _humanoid_ (it has two legs,
two arms and a head)

With rare exceptions, humanoid models have the same basic structure. This
structure represents the major articulated parts of the body: the head and
limbs. The first step to using Unity’s [Humanoid animation
features](ConfiguringtheAvatar.html) is to [set up and configure](class-
Avatar.html) an **Avatar** An interface for retargeting animation from one rig
to another. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar). Unity uses the Avatar to map the
simplified humanoid bone structure to the actual bones present in the Model’s
skeleton.

**Property:** | **Function:**  
---|---  
**Avatar Definition** | Choose where to get the Avatar definition.  
| **Create from this model** | Create an Avatar based on this model  
| **Copy from Other Avatar** | Point to an Avatar set up on another model.  
**Source** | Copy another Avatar with an identical rig to import its animation clips.   
  
Only available if the **Avatar Definition** is set to **Copy from Other
Avatar**.  
**Configure…** | Open the [Avatar configuration](class-Avatar.html).   
  
Only available if the **Avatar Definition** is set to **Create From This
Model**.  
**Skin Weights** | This property is identical for both Humanoid and Generic Models. See the documentation on Skin Weights above for information about it.  
**Optimize Game Object** | Remove and store the GameObject Transform hierarchy of the imported character in the Avatar and Animator component. If enabled, the SkinnedMeshRenderers of the character use the Unity animation system’s internal skeleton, which improves the performance of the animated characters.   
  
Only available if the **Avatar Definition** is set to **Create From This
Model**.  
**Extra Transforms to Expose** | Specify which Transform paths you want Unity to ignore when **Optimize Game Object** is enabled. For more information, see Including extra Transforms.  
  
This section only appears when **Optimize Game Object** is enabled.  
  
## Including extra Transforms

When you enable the **Optimize Game Object** property, Unity ignores any
Transform which is part of the hierarchy but is not mapped in the Avatar, in
order to improve CPU performance. However, you can mark specific nodes in the
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) hierarchy to include in
calculations using the **Extra Transforms to Expose** section:

![The Extra Transforms to Expose property appears when Optimize Game Objects
is enabled](../uploads/Main/ExtraTransforms.png) The Extra Transforms to
Expose property appears when Optimize Game Objects is enabled

**(A)** Enter the full or partial name in the search box to filter the list of
Transforms. This makes it easier to navigate through characters with a large
number of bones.

**(B)** Enable each Transform (bones of a skeleton) you want Unity to include
in calculations.

**(C)** Use the buttons to help select specific Transforms. For example, the
**Toggle All** button selects or deselects everything at once (regardless of
the current selection, including filtered items).

**(D)** Use the **Revert** button to undo your selections or the **Apply**
button to apply the exceptions to the Model.

**Note** : In optimized mode, skinned Mesh matrix extraction is multi-
threaded.

## Legacy animation types

![Your rig uses the Legacy Animation System](../uploads/Main/Rig-3.png) Your rig uses the Legacy Animation System **Property:** | **Function:**  
---|---  
**Generation** | Select the animation import method.  
| **Don’t Import** | Do not import animation  
| **Store in Original Roots (Deprecated)** | Deprecated. Do not use.  
| **Store in Nodes (Deprecated)** | Deprecated. Do not use.  
| **Store in Root (Deprecated)** | Deprecated. Do not use.  
| **Store in Root (New)** | Import the animation and store it in the Model’s root node. This is the default setting.  
**Skin Weights** | See the documentation on Skin Weights above for information about this property.  
  
For more information about legacy animation, see the documentation for [Legacy
Animation System](Animations.html).

* * *

  * **Skin Weights** added in [2019.1](https://docs.unity3d.com/2019.1/Documentation/Manual/30_search.html?q=newin20191) NewIn20191
  * **Materials** An asset that defines how a surface should be rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material) tab added in
[2017.2](https://docs.unity3d.com/2017.2/Documentation/Manual/30_search.html?q=newin20172)
NewIn20172

[](FBXImporter-Model.html)

Model tab

[](class-Avatar.html)

Avatar Mapping tab

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

