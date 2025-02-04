[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/occlusion-culling-window.html)
  * [中文](/cn/current/Manual/occlusion-culling-window.html)
  * [日本語](/ja/current/Manual/occlusion-culling-window.html)
  * [한국어](/kr/current/Manual/occlusion-culling-window.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/occlusion-culling-window.html)
  * [中文](/cn/current/Manual/occlusion-culling-window.html)
  * [日本語](/ja/current/Manual/occlusion-culling-window.html)
  * [한국어](/kr/current/Manual/occlusion-culling-window.html)

  * [Working in Unity](working-in-unity.html)
  * [Cameras](Cameras.html)
  * [Excluding hidden objects with occlusion culling](OcclusionCulling-landing.html)
  * Occlusion Culling window reference

[](class-OcclusionPortal.html)

Control occlusion in areas with Occlusion Portals

[](CullingGroupAPI-landing.html)

Configure culling with the CullingGroup API

# Occlusion Culling window reference

Open the Occlusion Culling window by navigating to the top menu and selecting
**Window** > **Rendering** > **Occlusion Culling** A process that disables
rendering GameObjects that are hidden (occluded) from the view of the camera.
[More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#Occlusionculling).

The Occlusion Culling window has 3 tabs: **Object** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#Object), **Bake** , and **Visualization**. In
addition to this, when both the Occlusion Culling window and the **Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view are visible, the Occlusion Culling
popup is visible in the **Scene view** An interactive view into the world you
are creating. You use the Scene View to select and position scenery,
characters, cameras, lights, and all other types of Game Object. [More
info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView).

## Object tab

![Occlusion Culling Window for a Mesh
Renderer](../uploads/Main/OcclusionCullingInspectorObject.png) Occlusion
Culling Window for a Mesh Renderer

In the **Object** tab, you can click the **All** , **Renderers** , and
**Occlusion Areas** buttons to filter the contents of the Hierarchy window.

When the **Renderers** filter is active, select a Renderer in the Hierarchy
window or Scene view to view and change its occlusion culling settings in the
Occlusion Culling window.

When the **Occlusion Areas** filter is active, you can select an Occlusion
Area in the Hierarchy window or Scene view to view and change its **Is View
Volume** setting in the Occlusion Culling window. You can also click Create
New Occlusion Area to create a new Occlusion Area in the Scene.

## Bake tab

In the **Bake** tab, you can fine-tune the parameters of the Occlusion Culling
bake process. Configure these settings to find a balance between bake times,
data size at runtime, and visual results.

The **Set Default Parameters** button resets the parameters to the default
values.

![Occlusion culling inspector bake tab.](../uploads/Main/OcclusionCullingInspectorBake.png) Occlusion culling inspector bake tab. Setting | Description  
---|---  
**Smallest Occluder** | The size of the smallest GameObject that can occlude other GameObjects, in metres. In general, for the smallest file size and fastest bake times, you should choose the highest value that gives good results in your Scene.  
**Smallest Hole** | The diameter of the smallest gap through which a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) can see, in metres. In general, for
the smallest file size and fastest bake times, you should choose the highest
value that gives good results in your Scene.  
**Backface Threshold** | If you need to reduce the size of the baked data, Unity can sample the Scene as it bakes, and exclude parts of the Scene where the visible occluder geometry consists of more than a given percentage of backfaces. An area with a high percentage of backfaces is likely to be underneath or inside geometry, and therefore not likely somewhere the Camera is at runtime. The default value of 100 never removes areas from the data. Lower values result in a smaller file size, but can lead to visual artifacts.  
  
At the bottom of the Bake tab are the **Bake** and **Clear** buttons. Click
the **Bake** button to bake occlusion culling data. Click the **Clear** button
to remove previously baked data.

## Visualization tab

When you select a Camera in the Scene view or Hierarchy window while the
**Visualization** tab is visible, Unity updates the Scene view to show the
effects of occlusion culling from the perspective of the selected Camera. You
can use the Occlusion Culling popup in the Scene view to configure the
visualization.

## Occlusion Culling popup in the Scene view

The Occlusion Culling popup has two modes: **Edit** , and **Visualization**.
You can switch between them using the drop-down menu.

### Edit mode

Setting | Description  
---|---  
**View Volumes** | When this is enabled, the Scene view contains blue lines that show the cells in the occlusion culling data. The cell size is affected by the **Smallest Occluder** setting: a lower value results in more, smaller cells, which in turn results in increased precision, and a larger file size.  
  
## Visualize mode

**Visualize** mode allows you to preview the results of occlusion culling from
the perspective of a given Camera. If you have a Camera selected, the preview
relates to that Camera. Otherwise, the preview relates to the last Camera that
you selected while in Visualize mode.

Setting | Description  
---|---  
**Camera Volumes** | When this is enabled, you can see yellow lines that indicate the area of the Scene for which Unity has generated occlusion culling data. This is determined based on Scene geometry, and on any View Volumes that you have defined in your Scene using Occlusion Areas. When the Camera is outside of the yellow lines, Unity does not perform occlusion culling.  
  
You can also see grey lines that indicate the cell in the occlusion culling
data that the Camera’s current position corresponds to, and the subdivisions
within the current cell. The **Smallest Hole** setting defines the minimum
size of the subdivisions within cells: a lower value results in more, smaller
subdivisions per cells, which in turn results in increased precision, and a
larger file size.  
**Visibility Lines** | When this is enabled, you can see green lines that indicate what the currently selected Camera can see.  
**Portals** | When this is enabled, you can see lines that represent connections between cells in the occlusion data. The currently visible portals are the ones that the currently selected Camera can see.  
  
[](class-OcclusionPortal.html)

Control occlusion in areas with Occlusion Portals

[](CullingGroupAPI-landing.html)

Configure culling with the CullingGroup API

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

