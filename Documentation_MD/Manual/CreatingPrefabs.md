[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/CreatingPrefabs.html)
  * [中文](/cn/current/Manual/CreatingPrefabs.html)
  * [日本語](/ja/current/Manual/CreatingPrefabs.html)
  * [한국어](/kr/current/Manual/CreatingPrefabs.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/CreatingPrefabs.html)
  * [中文](/cn/current/Manual/CreatingPrefabs.html)
  * [日本語](/ja/current/Manual/CreatingPrefabs.html)
  * [한국어](/kr/current/Manual/CreatingPrefabs.html)

  * [Working in Unity](working-in-unity.html)
  * [Working with GameObjects](working-with-gameobjects.html)
  * [Prefabs](Prefabs.html)
  * Creating Prefabs

[](Prefabs.html)

Prefabs

[](EditingInPrefabMode.html)

Editing a Prefab in Prefab Mode

# Creating Prefabs

In Unity’s **Prefab** An asset type that allows you to store a GameObject
complete with components and properties. The prefab acts as a template from
which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) system, **Prefab Assets** act as
templates. You create Prefab Assets in the Editor, and they are saved as an
Asset in the **Project window** A window that shows the contents of your
`Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow). From **Prefab Assets** , you
can create any number of **Prefab instances**. Prefab instances can either be
created in the editor and saved as part of your **Scenes** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), or instantiated at runtime.

## Creating Prefab Assets

To create a Prefab Asset, drag a **GameObject** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) from the Hierarchy window into the
Project window. The GameObject, and all its components and child GameObjects,
becomes a new Asset in your Project window. Prefabs Assets in the Project
window are shown with a thumbnail view of the GameObject, or the blue cube
Prefab icon, depending on how you have set up your Project window.

![Two prefabs \(FatBlob and “Key”\) shown in the Project window in two-column
view \(left\) and one-column view
\(right\)](../uploads/Main/PrefabsInProjectWindow1.png) Two prefabs (“FatBlob”
and “Key”) shown in the Project window in two-column view (left) and one-
column view (right)

This process of creating the Prefab Asset also turns the original GameObject
into a Prefab instance. It is now an instance of the newly created Prefab
Asset. Prefab instances are shown in the Hierarchy in blue text, and the root
GameObject of the Prefab is shown with the blue cube Prefab icon, instead of
the red, green and blue GameObject icon.

![A Prefab instance \(Key\) in the
scene](../uploads/Main/PrefabInstanceInScene1.png) A Prefab instance (Key) in
the scene

## Creating multiple Prefab Assets

To create multiple Prefab Assets at once, drag multiple GameObjects from the
Hierarchy window into the Project window. This functionality is the same as in
the above paragraph.

If you drag multiple GameObjects that are not already Prefabs into the Project
window, Unity creates new original Prefab Assets for each one without any
additional steps.

If any of the GameObjects you drag into the Project Window are existing Prefab
variants or Model Variants, Unity displays a dialog box which asks you to
confirm whether you want to create new Prefab Assets or new variants from the
GameObjects. The content of this dialog box changes depending on the number
and type of GameObjects you drag into the Project window.

## Creating Prefab instances

You can create instances of the Prefab Asset in the Editor by dragging the
Prefab Asset from the Project view to the Hierarchy or **Scene view** An
interactive view into the world you are creating. You use the Scene View to
select and position scenery, characters, cameras, lights, and all other types
of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView).

![Dragging a Prefab Key into the
Scene](../uploads/Main/PrefabsDragIntoScene1.png) Dragging a Prefab “Key” into
the Scene

You can also create instances of Prefabs at runtime using scripting. For more
information, see [Instantiating
Prefabs](https://docs.unity3d.com/Manual/instantiating-prefabs.html).

## Replacing existing prefabs

You can replace a Prefab by dragging a new GameObject from the Hierarchy
window and dropping it on top of an existing Prefab asset in the Project
window.

If you are replacing an existing Prefab, Unity tries to preserve references to
the Prefab itself and the individual parts of the Prefab such as child
GameObjects and Components. To do this, it matches the names of GameObjects
between the new Prefab and the existing Prefab that you are replacing.

**Note:** _Because this matching is done by name only, if there are multiple
GameObjects with the same name in the Prefab’s hierarchy, it is not possible
to predict which will be matched. Therefore if you need to ensure your
references are preserved when saving over an existing prefab, you must ensure
all GameObjects within the Prefab have unique names._

**Also note:** _You may encounter a similar problem in the case of preserving
references to existing Components when you save over an existing Prefab, if a
single GameObject within the Prefab has more than one of the same Component
type attached. In this case it is not possible to predict which of them will
be matched to the existing references._

* * *

  * 2018–07–31 Page published 

  * Nested Prefabs and Prefab Variants added in 2018.3

[](Prefabs.html)

Prefabs

[](EditingInPrefabMode.html)

Editing a Prefab in Prefab Mode

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

