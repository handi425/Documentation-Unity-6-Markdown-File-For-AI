[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UIE-Runtime-Panel-Settings.html)
  * [中文](/cn/current/Manual/UIE-Runtime-Panel-Settings.html)
  * [日本語](/ja/current/Manual/UIE-Runtime-Panel-Settings.html)
  * [한국어](/kr/current/Manual/UIE-Runtime-Panel-Settings.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UIE-Runtime-Panel-Settings.html)
  * [中文](/cn/current/Manual/UIE-Runtime-Panel-Settings.html)
  * [日本語](/ja/current/Manual/UIE-Runtime-Panel-Settings.html)
  * [한국어](/kr/current/Manual/UIE-Runtime-Panel-Settings.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [UI Toolkit](UIElements.html)
  * [Support for runtime UI](UIE-support-for-runtime-ui.html)
  * [Configure runtime UI](UIE-render-runtime-ui.html)
  * Panel Settings properties reference

[](UIE-create-panel.html)

Create a panel

[](UIE-create-ui-document-component.html)

UI Document component

# Panel Settings properties reference

The following tables describe the Panel Settings asset properties:

**Property** | **Description**  
---|---  
**Theme Style Sheet** | Apply a default [TSS file](UIE-tss.html) to every **UI**(User Interface) Allows a user to interact with your application. Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Document that the panel renders.  
**Text Settings** | Set the [UITK Text Settings](UIE-text-setting-asset.html) asset for this panel. If this asset isn’t set, UI Toolkit automatically creates one with the default settings.  
**Binding Console Logs** | Set the [binding log levels](UIE-runtime-binding-logging-levels.html).  
**Target Texture** | Set the [render texture](class-RenderTexture.html)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture) for the panel.  
  
For a 3D game, display UI on 3D geometry in the scene.  
**Target Display** | Set the display for the panel. Only set this if the target texture isn’t set, as the target texture takes precedence over the target display.  
**Sort Order** | Set the order that the UI System draws panels in if the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) uses more than one panel. Panels with
higher **Sort Order** values are drawn on top of panels with lower values.  
**Scale Mode** | Set how the panel’s UI scales when the screen size changes.  
**Scale Mode Parameters** | Display different properties depending on the **Scale Mode** setting.  
**Dynamic Atlas Settings** | Specify the settings that the dynamic atlas system uses.  
| **Min Atlas Size** | Set the minimum size (width/height) of the atlas texture, in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel).  
| **Max Atlas Size** | Set the maximum size (width/height) of the atlas texture, in pixels.  
| **Max Sub Texture Size** | Set the maximum size (width/height) of a texture that can be added to the atlas.  
| **Active Filters** | Set the filters that the dynamic atlas system uses to exclude textures from the texture atlas.  
**Clear Settings** | Set how the panel clears before rendering.  
| **Clear Color** | Set whether the panel clears the color buffer before rendering.  
| **Clear Color Value** | Set the color that the panel uses to clear the color buffer.  
| **Clear Depth Stencil** | Set whether the panel clears the depth stencil before rendering.  
**Buffer Management** | Set how the panel manages its buffers.  
| **Vertex budget** | Set the approximate number of vertices the panel uses. This helps initialize vertex buffers with the right size which can reduce draw calls. A value of `0` uses the default value for UI rendering.  
  
## Scale Mode parameters

The following table describes the parameters for each scale mode:

**Scale Mode** | **Scale Mode Parameters** | **Description**  
---|---|---  
**Constant Pixel Size** |  | Set elements to stay the same size, in pixels, regardless of screen size.  
| **Scale** | Multiply element sizes by this value. Must be greater than 0.  
**Constant Physical Size** |  | Set elements stay the same physical size regardless of screen size and resolution.  
| **Reference DPI** | Set the **Reference DPI** value to the screen density that your UI was designed for. When the system renders your UI, it tries to find the actual DPI value of the screen, and compares it to the **Reference DPI**. If they’re different, the system scales the UI accordingly.  
| **Fallback DPI** | Use this value if the UI system can’t determine the screen DPI.  
**Scale with Screen Size** |  | Set elements to grow or shrink depending on the screen size.  
| **Screen Match Mode** | Set how to scale elements when the screen resolution is different from the **Reference Resolution** :  
  

  * **Match Width or Height** : Scale the canvas area with the width or the height as reference, or a linear interpolation between the width and the height.
  * **Shrink** : Crop the canvas area either horizontally or vertically, so the size of the canvas is smaller than the reference. 
  * **Expand** : Expand the canvas area either horizontally or vertically, so the size of the canvas is larger than the reference.

  
| **Reference Resolution** | Set the resolution that this panel’s UI is designed for. If the screen resolution is larger than the reference resolution, the UI scales up. If it’s smaller, the UI scales down. How the UI scales depends on the **Screen Match Mode**.  
| **Screen Match Mode Parameters** | When **Screen Match Mode** is set to **Match Width or Height** , the **Match** value controls whether the UI system scales the UI to match the screen width, the screen height, or a mix of the two.   
  
For example, if the value is `0`, it matches the width; if the value is `1`,
it matches the height; if the value is `0.4`, it linearly interpolates between
width and height by `40%`.  
  
## Active Filters

You can apply more than one filter at a time. The following table describes
each active filter.

**Filter** | **Description**  
---|---  
**Nothing** | Disable all the filters.  
**Everything** | Apply all the filters.  
**Readability** | Exclude textures that [`Texture2D.isReadable`](../ScriptReference/Texture-isReadable.html) is set to `true`.   
Unity can’t automatically update the dynamic atlas when you add a texture
through APIs like
[`Texture2D.SetPixels`](../ScriptReference/Texture2D.SetPixels.html). You can
use
[`RuntimePanelUtils.SetTextureDirty`](../ScriptReference/UIElements.RuntimePanelUtils.SetTextureDirty.html)
to force the atlas to update its content for a given texture.  
**Size** | Exclude textures that are larger than the **Max Sub Texture Size** setting.   
Large textures can saturate the atlas quickly. If you don’t want to add large
textures to the atlas, select this filter and adjust **Max Sub Texture Size**
to fit your needs. By default, textures larger than `64x64` aren’t allowed
into the atlas.  
**Format** | Store sRGB-encoded data with 8-bits per channel precision, and excludes sub-textures that would lose precision or be truncated when added to the atlas, such as an R16G16B16A16_FLOAT texture.  
**Color Space** | Exclude R8G8B8A8_UNORM content when the project is in a linear color space.   
In a linear color space, the format of the
[`RenderTexture`](../ScriptReference/RenderTexture.html) of the dynamic atlas
is R8G8B8A8_SRGB. The data stored in the
[`RenderTexture`](../ScriptReference/RenderTexture.html) is sRGB-encoded. When
read from, it’s linearized, and when written to, it’s encoded to sRGB. Because
of the limited precision of the format, R8G8B8A8_UNORM content stored in the
atlas could cause banding to occur.  
**Filter Mode** | Exclude textures for which the sub-texture filter mode, such as Point or Bilinear, doesn’t match the atlas filter mode. This prevents the mismatch between the sub-texture filter mode and the atlas filter mode. The mismatch could cause unexpected blurriness or blockiness.  
  
## Additional resources

  * [Get started with runtime UI](UIE-get-started-with-runtime-ui.html)
  * [Render UI in the Game view](UIE-render-runtime-ui.html)
  * [Runtime event system](UIE-Runtime-Event-System.html)
  * [FAQ for input and event systems with UI Toolkit](UIE-faq-event-and-input-system.html)
  * [Performance consideration for runtime UI](UIE-performance-consideration-runtime.html)
  * [`PanelSettings`](../ScriptReference/UIElements.PanelSettings.html)

[](UIE-create-panel.html)

Create a panel

[](UIE-create-ui-document-component.html)

UI Document component

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

