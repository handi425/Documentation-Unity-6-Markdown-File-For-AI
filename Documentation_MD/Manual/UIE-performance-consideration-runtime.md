[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-performance-consideration-runtime.html)
  * [中文](/cn/current/Manual/UIE-performance-consideration-runtime.html)
  * [日本語](/ja/current/Manual/UIE-performance-consideration-runtime.html)
  * [한국어](/kr/current/Manual/UIE-performance-consideration-runtime.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-performance-consideration-runtime.html)
  * [中文](/cn/current/Manual/UIE-performance-consideration-runtime.html)
  * [日本語](/ja/current/Manual/UIE-performance-consideration-runtime.html)
  * [한국어](/kr/current/Manual/UIE-performance-consideration-runtime.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Support for runtime UI](UIE-support-for-runtime-ui.html)
  * Performance consideration for runtime UI

[](UIE-faq-event-and-input-system.html)

FAQ for input and event systems with UI Toolkit

[](UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)

Use usage hints to reduce draw calls and geometry regeneration

# Performance consideration for runtime UI

This section describes how you can improve the performance for runtime
**UI**(User Interface) Allows a user to interact with your application. Unity
currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI).

**Topic** | **Description**  
---|---  
[Use usage hints to reduce draw calls and geometry regeneration](UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html) | Use usage hints to set how an element is used at runtime. Usage hints can reduce draw calls and avoid geometry regeneration.  
[Control textures of the dynamic atlas](UIE-control-textures-of-the-dynamic-atlas.html) | Use an atlas to reduce the number of batches broken by texture changes and achieve good performance.  
[Platform and mesh consideration](UIE-platform-and-mesh.html) | Consider device capabilities and avoid **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) tessellation.  
  
## Additional resources

  * [Panel Settings asset](UIE-Runtime-Panel-Settings.html)
  * [`usageHints`](../ScriptReference/UIElements.VisualElement-usageHints.html)

[](UIE-faq-event-and-input-system.html)

FAQ for input and event systems with UI Toolkit

[](UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)

Use usage hints to reduce draw calls and geometry regeneration

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

