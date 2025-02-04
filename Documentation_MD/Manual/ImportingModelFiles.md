[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ImportingModelFiles.html)
  * [中文](/cn/current/Manual/ImportingModelFiles.html)
  * [日本語](/ja/current/Manual/ImportingModelFiles.html)
  * [한국어](/kr/current/Manual/ImportingModelFiles.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ImportingModelFiles.html)
  * [中文](/cn/current/Manual/ImportingModelFiles.html)
  * [日本語](/ja/current/Manual/ImportingModelFiles.html)
  * [한국어](/kr/current/Manual/ImportingModelFiles.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Models](models.html)
  * [Importing models into Unity](models-importing.html)
  * Importing a model

[](models-importing.html)

Importing models into Unity

[](ConfiguringtheAvatar.html)

Importing a model with humanoid animations

# Importing a model

Model files can contain a variety of data, such as meshes, animation rigs and
clips, materials and textures. Your file might not contain all of these
elements, but you can follow any portion of the workflow that you need to:

  1. Select the file in the Project view to see the Import Settings window
  2. Set any Model-specific or general importer options
  3. Set up options for importing Rigs and Animation (not available for SpeedTree Models)
  4. Dealing with Materials and Textures
  5. Drag the file into Unity

For guidelines on how to export _Humanoid_ animation from your 3D modeling
software, see [Preparing Humanoid Models for export](UsingHumanoidChars.html).

**Note:** Unity’s primary support for **Model files** A file containing a 3D
data, which may include definitions for meshes, bones, animation, materials
and textures. [More info](3D-formats.html)  
See in [Glossary](Glossary.html#Modelfile) is the FBX format. However, you can
save your 3D files from most common 3D modeling software in their native
format (for example, .max, .blend, .mb, .ma). When Unity finds these file
types in your `Assets` folder, it calls your 3D modeling software’s FBX export
**plug-in** A set of code created outside of Unity that creates functionality
in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-
ins (managed .NET assemblies created with tools like Visual Studio) and Native
plug-ins (platform-specific native code libraries). [More info](./plug-
ins.html)  
See in [Glossary](Glossary.html#Plug-in), and imports the file. The 3D
modeling software must be installed on the same computer as Unity, so in most
cases it’s best practice to directly export as FBX from your application into
your `Assets` folder.

## Accessing the Import Settings window

No matter what kind of data you want to extract from the Model file, you
always start the same way:

  1. Open the **Project** In Unity, you use a project to design and develop a game. A project stores all of the files that are related to a game, such as the asset and Scene files. [More info](2Dor3D.html)  
See in [Glossary](Glossary.html#Project) window and the **Inspector** A Unity
window that displays information about the currently selected GameObject,
asset or project settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) so that you can see both at once.

  2. Select the **Model** A 3D model representation of an object, such as a character, a building, or a piece of furniture. [More info](3D-formats.html)  
See in [Glossary](Glossary.html#Model) file you want to import from the
**Asset** Any media or data that can be used in your game or project. An asset
may come from a file created outside of Unity, such as a 3D Model, an audio
file or an image. You can also create some asset types in Unity, such as an
Animator Controller, an Audio Mixer or a Render Texture. [More
info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#Asset) folder in the **Project** window.

The **Import Settings** window opens in the **Inspector** showing the **Model
tab** by default.

## Setting Model-specific and general importer options

The options that are available for SpeedTree Models vs. other Models are very
different. For more information, see the [SpeedTree Model
tab](SpeedTreeImporter-Model.html).

Character and animated Models provide diverse options on [their Model
tab](FBXImporter-Model.html), which allow you to:

  * Use the **Scale Factor** and **Convert Units** properties to adjust how Unity interprets units. For example, 3ds Max uses 1 unit to represent 10 centimeters, whereas Unity uses 1 unit to represent 1 meter.
  * Use the **Mesh Compression** , **Read/Write Enabled** , **Optimize Mesh** , **Keep Quads** , **Index Format** , or **Weld Vertices** properties to reduce resources and save memory.
  * You can enable the **Import BlendShapes** option if the Model file came from Maya or 3ds Max, or any other 3d modeling application that supports morph target animation.
  * You can enable the **Generate Colliders** option for environment geometry.
  * You can enable specific FBX settings, such as **Import Visibility** , or **Import Cameras** and **Import Lights**.
  * For Model files that contain only Animation, you can enable the **Preserve Hierarchy** option to prevent hierarchy mismatch in your skeleton.
  * You can set the **Swap UVs** and **Generate Lightmap UVs** if you are using a **Lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap).

  * You can exercise control over how Unity handles the Normals and Tangents in your Model with the **Normals** The direction perpendicular to the surface of a mesh, represented by a Vector. Unity uses normals to determine object orientation and apply shading. [More info](scripting-vectors.html)  
See in [Glossary](Glossary.html#Normal), **Normals Mode** , **Tangents** , or
**Smoothing Angle** options.

## Setting options for importing Rigs and Animation

If your file contains Animation data, you can follow the guidelines for
setting up the Rig using the [Rig tab](FBXImporter-Rig.html) and then
extracting or defining **Animation Clips** Animation data that can be used for
animated characters or simple animations. It is a simple “unit” piece of
motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More
info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) using the [Animation
tab](class-AnimationClip.html). The workflow differs between Humanoid and
Generic (non-Humanoid) animation types because Unity needs the Humanoid’s bone
structure to be very specific, but only needs to know which bone is the **root
node** A transform in an animation hierarchy that allows Unity to establish
consistency between Animation clips for a generic model. It also enables Unity
to properly blend between Animations that have not been authored “in place”
(that is, where the whole Model moves its world position while animating).
[More info](AnimationRootMotionNodeOnImportedClips.html)  
See in [Glossary](Glossary.html#Rootnode) for the Generic type:

  * [Humanoid-type workflow](ConfiguringtheAvatar.html)
  * [Generic-type workflow](GenericAnimations.html)

> **Note:** SpeedTree Models have neither a **Rig** nor an **Animation** tab.

## Dealing with Materials and Textures

If your file contains materials and textures, you can define how you want to
deal with them:

  1. Click [the Materials tab](FBXImporter-Materials.html) in the **Import Settings** window.
  2. From the [Material Creation Mode](FBXImporter-Materials.html) drop-down menu, choose how you want to import the Materials from the FBX file. Unless you chose **None** , several options appear in the **Materials** An asset that defines how a surface should be rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material) tab, including the **Location**
option, whose value determines what the other options are.

  3. Choose the **Use Embedded Materials** option to [keep the Materials inside the imported Asset](FBXImporter-Materials.html#Embedded).
  4. When you have finished setting the options, click the **Apply** button at the bottom of the **Import Settings** window to save them or click the **Revert** button to cancel.

### Finding textures

Unity follows a specific search plan to automatically look for textures on
import. First, the importer looks for a sub-folder called Textures within the
same folder as the **mesh** The main graphics primitive of Unity. Meshes make
up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh), or in any parent folder. If this fails,
Unity performs an exhaustive search of all textures in the project. Although
slightly slower, the main disadvantage of the exhaustive search is that there
could be two or more textures in the project with the same name. In this case,
it is not guaranteed that Unity can find the right one.

![Place your textures in a Textures folder at or above the assets
level](../uploads/Main/Mesh-TextureImportHierarchy.png) Place your textures in
a **Textures** folder at or above the asset’s level

**(A)** Possible places to find Textures

**(B)** Mesh being imported

### Normal maps

If you have a character with a **normal map** A type of Bump Map texture that
allows you to add surface detail such as bumps, grooves, and scratches to a
model which catch the light as if they are represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap) that was generated from a high-
polygon version of the Model, you should import the game-quality version with
a [Smoothing Angle](FBXImporter-Model.html#geoprops) of 180 degrees. This
prevents odd-looking seams in lighting due to tangent splitting. If the seams
are still present with these settings, choose [Calculate Legacy With Split
Tangents](FBXImporter-Model.html#geoprops) from the **Tangents** drop-down
menu. If you are converting a greyscale image into a normal map, you don’t
need to worry about this.

## Drag the file into Unity

Finally, you can import the file into your scene:

  * If it contains a Mesh, drag the file into the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view to instantiate it as a **Prefab**
An asset type that allows you to store a GameObject complete with components
and properties. The prefab acts as a template from which you can create new
object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) for a **GameObject** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

  * If it contains Animation Clips, you can drag the file into [the Animator window](AnimatorWindow.html) to use in [the State Machine](StateMachineBasics.html). You can also drag the Animation take directly onto an instantiated Prefab in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView). This automatically creates an
Animation Controller and connects the animation to the Model.

[](models-importing.html)

Importing models into Unity

[](ConfiguringtheAvatar.html)

Importing a model with humanoid animations

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

