[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-control-textures-of-the-dynamic-atlas.html)
  * [中文](/cn/current/Manual/UIE-control-textures-of-the-dynamic-atlas.html)
  * [日本語](/ja/current/Manual/UIE-control-textures-of-the-dynamic-atlas.html)
  * [한국어](/kr/current/Manual/UIE-control-textures-of-the-dynamic-atlas.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-control-textures-of-the-dynamic-atlas.html)
  * [中文](/cn/current/Manual/UIE-control-textures-of-the-dynamic-atlas.html)
  * [日本語](/ja/current/Manual/UIE-control-textures-of-the-dynamic-atlas.html)
  * [한국어](/kr/current/Manual/UIE-control-textures-of-the-dynamic-atlas.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Support for runtime UI](UIE-support-for-runtime-ui.html)
  * [Performance consideration for runtime UI](UIE-performance-consideration-runtime.html)
  * Control textures of the dynamic atlas

[](UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)

Use usage hints to reduce draw calls and geometry regeneration

[](UIE-platform-and-mesh.html)

Platform and mesh considerations

# Control textures of the dynamic atlas

To reduce the number of batches broken by texture changes and achieve good
performance, use an atlas to group together textures used at the same time.
You can achieve this with either of the following methods:

  * Use a [sprite atlas](sprite/atlas/atlas-landing.html)A utility that packs several sprite textures tightly together within a single texture known as an atlas. [More info](sprite/atlas/v2/v2-landing.html)  
See in [Glossary](Glossary.html#SpriteAtlas). With this method, you have more
control over the sprites but you need to manually create the **sprite** A 2D
graphic objects. If you are used to working in 3D, Sprites are essentially
just standard textures but there are special techniques for combining and
managing sprite textures for efficiency and convenience during development.
[More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) atlas.

  * Use a dynamic atlas. **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Toolkit automatically adds textures to, or
removes textures from, a dynamic atlas when **visual elements** A node of a
visual tree that instantiates or derives from the C#
[`VisualElement`](../ScriptReference/UIElements.VisualElement.html) class. You
can style the look, define the behaviour, and display it on screen as part of
the UI. [More info](UIE-VisualTree.html)  
See in [Glossary](Glossary.html#Visualelement) reference them.

## Verify textures in dynamic atlas

When you use dynamic atlas to group together textures, to limit the number of
[draw calls](DrawCallBatching.html), make sure that your textures enter the
dynamic atlas. To verify, use the [Frame Debugger](FrameDebugger.html). Frame
Debugger helps you to observe texture changes and deduce batch breaking.

The following example verifies that the dynamic atlas contains all the
textures in runtime UI.

![The example Dynamic Atlas window contains all the textures in runtime
UI.](../uploads/Main/uxml/dynamic-atlas.png) The example Dynamic Atlas window
contains all the textures in runtime UI.

## Apply built-in filters

The dynamic atlas texture starts from a specified minimum size, and grows as
needed, doubling horizontally or vertically, up to a specified maximum size.
You can define the [minimum and maximum atlas sizes](UIE-Runtime-Panel-
Settings.html#dynamic-atlas-setting) in the Panel Settings asset. You can also
use the filters in the dynamic atlas to decide whether to add a sub-texture to
the atlas.

To enable or disable the filters, in the Panel Settings asset’s Inspector
window, select the options from **Dynamic Atlas Settings** > [**Active
Filters**](UIE-Runtime-Panel-Settings.html#active-filters) dropdown list.

## Use custom filters

You can assign a custom filter to
[`PanelSettings.dynamicAtlasSettings.customFilter`](../ScriptReference/UIElements.DynamicAtlasSettings-
customFilter.html) to add or relax constraints on a global or per-texture
basis.

The following custom filter example bypasses a large texture from the
[**Size**](UIE-Runtime-Panel-Settings.html#active-filters) filter while
keeping the [**Size**](UIE-Runtime-Panel-Settings.html#active-filters) filter
active for other textures:

    
    
    using UnityEngine;
    using UnityEngine.UIElements;
    
    class MyCustomFilter : MonoBehaviour
    {
        public PanelSettings panelSettings;
        public Texture2D largeTexture;
    
        void OnEnable() { panelSettings.dynamicAtlasSettings.customFilter = Filter; }
    
        void OnDisable() { panelSettings.dynamicAtlasSettings.customFilter = null; }
    
        bool Filter(Texture2D texture, ref DynamicAtlasFilters filtersToApply)
        {
            if (texture == largeTexture)
            {
                // Disable the Size check for this one.
                filtersToApply &= ~DynamicAtlasFilters.Size;
            }
            return true;
        }
    }
    

## Manage dynamic atlas size

When new elements appear in the UI, their textures are added to the dynamic
atlas until the atlas reaches or exceeds the Max Atlas Size specified in the
Dynamic Atlas Settings.

On devices with limited memory, you might need to set a lower Max Atlas Size
than the default, such as `2048` **pixels** The smallest unit in a computer
image. Pixel size depends on your screen resolution. Pixel lighting is
calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) instead of `4096` pixels.

## Manage dynamic atlas fragmentation

When textures are added or removed from the atlas, it can lead to
fragmentation, creating small spaces where previous textures were, which are
too small to reallocate to other textures.

To maximize the usage of the atlas and avoid fragmentation, you need to
manually reset its contents by calling the
[`RuntimePanelUtils.ResetDynamicAtlas()`](../ScriptReference/UIElements.RuntimePanelUtils-
ResetDynamicAtlas.html) extension method, which requires accessing the `panel`
property of a `VisualElement`.

Consider resetting the dynamic atlas based on your application’s behaviour,
for example when you remove or add large amounts of visual elements.

The following example shows how to use the
[`RuntimePanelUtils.ResetDynamicAtlas()`](../ScriptReference/UIElements.RuntimePanelUtils.ResetDynamicAtlas.html)
extension method:

    
    
    using UnityEngine;
    using UnityEngine.UIElements;
    
    [RequireComponent(typeof(UIDocument))]
    class DynamicAtlasResetExample : MonoBehaviour
    {
        VisualElement rootVisualElement => GetComponent<UIDocument>().rootVisualElement;
    
        public void OnEnable()
        {
            rootVisualElement.Add(new Button(ResetAtlas) { text = "Reset Dynamic Atlas"});
        }
    
        private void ResetAtlas()
        {
            rootVisualElement.panel.ResetDynamicAtlas();
        }
    
    }
    

## Additional resources

  * [Panel Settings asset](UIE-Runtime-Panel-Settings.html)
  * [Frame Debugger](FrameDebugger.html)
  * [Draw call batching](DrawCallBatching.html)
  * [Sprite Atlas](sprite/atlas/atlas-landing.html)

[](UIE-use-usage-hints-to-reduce-draw-calls-and-geometry-regeneration.html)

Use usage hints to reduce draw calls and geometry regeneration

[](UIE-platform-and-mesh.html)

Platform and mesh considerations

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

