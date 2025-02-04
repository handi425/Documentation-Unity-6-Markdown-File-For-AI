[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-OcclusionPortal.html)
  * [中文](/cn/current/Manual/class-OcclusionPortal.html)
  * [日本語](/ja/current/Manual/class-OcclusionPortal.html)
  * [한국어](/kr/current/Manual/class-OcclusionPortal.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-OcclusionPortal.html)
  * [中文](/cn/current/Manual/class-OcclusionPortal.html)
  * [日本語](/ja/current/Manual/class-OcclusionPortal.html)
  * [한국어](/kr/current/Manual/class-OcclusionPortal.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Excluding hidden objects with occlusion culling](OcclusionCulling-landing.html)
  * Control occlusion in areas with Occlusion Portals

[](class-OcclusionArea.html)

Create high-precision occlusion areas

[](occlusion-culling-window.html)

Occlusion Culling window reference

# Control occlusion in areas with Occlusion Portals

[Switch to Scripting](../ScriptReference/OcclusionPortal.html "Go to
OcclusionPortal page in the Scripting Reference")

An Occlusion Portal can either be open or closed. When an Occlusion Portal is
closed, it occludes other **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). When an Occlusion Portal is open,
it does not occlude other GameObjects.

If you have a GameObject in your **Scene** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) that has an open and a closed state
(such as a door), you can create an Occlusion Portal that represents it in the
**occlusion culling** A process that disables rendering GameObjects that are
hidden (occluded) from the view of the camera. [More
info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#Occlusionculling) system. You can then set the
open state of the Occlusion Portal according to the state of that GameObject.
An Occlusion Portal component does not need to be placed on the GameObject it
represents.

## Setting up an Occlusion Portal in your Scene

  1. Choose a suitable GameObject in your Scene to act as an Occlusion Portal. Good candidates for Occlusion Portals are medium to large solid GameObjects, such as a door.
  2. Ensure that the GameObject is not marked as Occluder Static or Occludee Static.
  3. Add an **Occlusion Portal** component to the GameObject.
  4. Bake the occlusion data for your Scene. See [Getting started with occlusion culling](occlusion-culling-getting-started.html) for instructions.
  5. Ensure that the Occlusion Culling window, the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) panel and the **Scene view** An
interactive view into the world you are creating. You use the Scene View to
select and position scenery, characters, cameras, lights, and all other types
of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) are all visible.

  6. In the Scene view, move the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) to a position where it is directly in
front of the Occlusion Portal.

  7. Select the GameObject with the Occlusion Portal component.
  8. In the Inspector window, toggle the Occlusion Portal component’s **Open** property on and off. In the Scene view, observe the difference in occlusion culling.

## Opening and closing an Occlusion Portal at runtime

Use a script to set the Occlusion Portal’s
[open](../ScriptReference/OcclusionPortal-open.html) property to the desired
state.

    
    
    void OpenDoor() {
         // Toggle the Occlusion Portal's open state, so that Unity renders the GameObjects behind it
        myOcclusionPortal.open = true;
        
        // Call a function that plays a door opening animation, or otherwise hides the GameObject
        …
    }
    

## Occlusion Portal component reference

![](../uploads/Main/OcclusionPortal.png) **_Property:_** | **_Function:_**  
---|---  
**Open** | If enabled, the Occlusion Portal is open, and does not occlude Renderers. If disabled, the Occlusion Portal is closed, and occludes Renderers.  
**Center** | Set the center of the Occlusion Portal. The default value is 0,0,0.  
**Size** | Define the size of the Occlusion Portal.  
  
OcclusionPortal

[](class-OcclusionArea.html)

Create high-precision occlusion areas

[](occlusion-culling-window.html)

Occlusion Culling window reference

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

