[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ProfilerGI.html)
  * [中文](/cn/current/Manual/ProfilerGI.html)
  * [日本語](/ja/current/Manual/ProfilerGI.html)
  * [한국어](/kr/current/Manual/ProfilerGI.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ProfilerGI.html)
  * [中文](/cn/current/Manual/ProfilerGI.html)
  * [日本語](/ja/current/Manual/ProfilerGI.html)
  * [한국어](/kr/current/Manual/ProfilerGI.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
  * [Creating lightmaps at runtime with Enlighten Realtime Global Illumination](realtime-gi-using-enlighten-landing.html)
  * Global Illumination Profiler module

[](LODRealtimeGI.html)

LOD and Enlighten Realtime Global Illumination

[](configure-lightmapping-settings.html)

Configuring lightmapping

# Global Illumination Profiler module

The **Global Illumination** A group of techniques that model both direct and
indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) **Profiler** A window that
helps you to optimize your game. It shows how much time is spent in the
various areas of your game. For example, it can report the percentage of time
spent rendering, animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) module displays statistics about how
much CPU time the [Enlighten Realtime Global Illumination](realtime-gi-using-
enlighten.html) subsystem uses across all worker threads. There is an option
to control the number of **Enlighten** A lighting system by Geomerics used in
Unity for Enlighten Realtime Global Illumination. [More
info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) worker threads included in [Command
Line Arguments](CommandLineArguments.html).

To open the Profiler window, go to menu: **Window > Analysis > Profiler**.

![Global Illumination Profiler module](../uploads/Main/gi-chart.png) Global
Illumination Profiler module

## Chart categories

The Global Illumination Profiler module’s chart tracks the time the global
illumination subsystem spent on all worker threads. The timings are divided
into 10 categories. To change the order of the categories in the chart, you
can drag and drop them in the chart’s legend. You can also click a category’s
colored legend to toggle its display.

**Chart** | **Description**  
---|---  
**Light Probe** | The time spent updating [Light Probes](LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe).  
**Setup** | The time spent in the Setup stage.  
**Environment** | The time spent processing Environment lighting.  
**Input Lighting** | The time spent processing input lighting.  
**Systems** | The time spent updating Systems.  
**Solve Tasks** | The time spent running [radiosity solver tasks](class-MeshRenderer.html).  
**Dynamic Objects** | Time spent updating Dynamic **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).  
**Other Commands** | Time spent updating other commands.  
**Block Command Write** | Time spent in a blocked state, waiting for the command buffer.  
  
## Module details pane

When you select the Global Illumination module, the details pane below it
displays a breakdown of where the application spent time in the selected
frame. The data available is as follows:

**Data** | **Description**  
---|---  
**Total CPU Time** | Total Enlighten Global Illumination CPU time across all threads in ms.  
**Probe Update Time** | Time spent updating Light Probes in ms.  
**Setup Time** | Time spent in the Setup stage in ms.  
**Environment Time** | Time spent processing Environment lighting in ms.  
**Input Lighting Time** | Time spent processing input lighting in ms.  
**Systems Time** | Time spent updating Systems in ms.  
**Solve Tasks Time** | Time spent running radiosity solver tasks in ms.  
**Dynamic Objects Time** | Time spent updating Dynamic GameObjects in ms.  
**Time Between Updates** | Time between Global Illumination updates in ms.  
**Other Commands Time** | Time spent processing other commands in ms.  
**Blocked Command Write Time** | Time spent in blocked state, waiting for command buffer in ms.  
**Blocked Buffer Writes** | Number of writes to the command buffer that were blocking.  
**Total Light Probes** | Total number of Light Probes in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).  
**Solved Light Probes** | Number of solved Light Probes since the last update.  
**Probe Sets** | Number of Light Probe sets in the Scene.  
**Systems** | Number of Enlighten Global Illumination Systems in the Scene.  
**Pending Material GPU Renders** | Number of Albedo/Emission renders queued for rendering on the GPU.  
**Pending Material Updates** | Number of Material updates waiting to get processed.  
  
## Additional resources

  * [Profiler window introduction](ProfilerWindow.html)
  * [Profiling your application](profiler-profiling-applications.html)

[](LODRealtimeGI.html)

LOD and Enlighten Realtime Global Illumination

[](configure-lightmapping-settings.html)

Configuring lightmapping

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

