[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)
  * [中文](/cn/current/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)
  * [日本語](/ja/current/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)
  * [한국어](/kr/current/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)
  * [中文](/cn/current/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)
  * [日本語](/ja/current/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)
  * [한국어](/kr/current/Manual/UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Support for runtime UI](UIE-support-for-runtime-ui.html)
  * [Performance consideration for runtime UI](UIE-performance-consideration-runtime.html)
  * Use usage hints to reduce draw calls and geometry regeneration

[](UIE-performance-consideration-runtime.html)

Performance consideration for runtime UI

[](UIE-control-textures-of-the-dynamic-atlas.html)

Control textures of the dynamic atlas

# Use usage hints to reduce draw calls and geometry regeneration

You can use usage hints to set how an element is used at runtime. Usage hints
can reduce draw calls and avoid geometry regeneration.

You can set the usage hints in **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Builder, UXML, or C#. The following
examples set the usage hints to `DynamicTransform`:

**UXML** :

    
    
    <ui:VisualElement usage-hints="DynamicTransform" />
    

**C#** :

    
    
    visualElement.usageHints = UsageHints.DynamicTransform;
    

The supported usage hints are:

  * [`DynamicTransform`](../ScriptReference/UIElements.UsageHints.DynamicTransform.html)
  * [`GroupTransform`](../ScriptReference/UIElements.UsageHints.GroupTransform.html)
  * [`MaskContainer`](../ScriptReference/UIElements.UsageHints.MaskContainer.html)
  * [`DynamicColor`](../ScriptReference/UIElements.UsageHints.DynamicColor.html)

## Additional resources

  * [`usageHints`](../ScriptReference/UIElements.UsageHints.html)
  * [`VisualElement.usageHints`](../ScriptReference/UIElements.VisualElement-usageHints.html)

[](UIE-performance-consideration-runtime.html)

Performance consideration for runtime UI

[](UIE-control-textures-of-the-dynamic-atlas.html)

Control textures of the dynamic atlas

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

