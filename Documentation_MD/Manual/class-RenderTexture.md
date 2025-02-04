[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-RenderTexture.html)
  * [中文](/cn/current/Manual/class-RenderTexture.html)
  * [日本語](/ja/current/Manual/class-RenderTexture.html)
  * [한국어](/kr/current/Manual/class-RenderTexture.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-RenderTexture.html)
  * [中文](/cn/current/Manual/class-RenderTexture.html)
  * [日本語](/ja/current/Manual/class-RenderTexture.html)
  * [한국어](/kr/current/Manual/class-RenderTexture.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Textures](Textures-landing.html)
  * [Textures reference](textures-reference.html)
  * Render Texture Inspector window reference

[](class-MovieTexture.html)

Movie Texture Inspector window reference

[](class-CustomRenderTexture.html)

Custom Render Texture Inspector window reference

# Render Texture Inspector window reference

[Switch to Scripting](../ScriptReference/RenderTexture.html "Go to
RenderTexture page in the Scripting Reference")

The **Render Texture** **inspector** A Unity window that displays information
about the currently selected GameObject, asset or project settings, allowing
you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) is similar to the [Texture
Inspector](class-TextureImporter.html).

The Render Texture inspector displays the current contents of Render Texture
in real-time and can be an invaluable debugging tool for effects that use
render textures.

**_Property:_** | **_Function:_**  
---|---  
**Dimension** | The dimensionality (type) of the render texture.  
| **2D** | The render texture is two-dimensional.  
| **Cube** | The render texture is a cube map.  
| **3D** | The render texture is three-dimensional.  
**Size** | The size of the render texture in **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel). You can only enter power-of-two
values, such as 128 and 256.  
**Anti-Aliasing** | The number of anti-aliasing samples. You can select **None** , **2 samples** , **4 samples** , or **8 samples**. If you select **None** , Unity does not apply anti-aliasing.  
**Enable Compatible Color Format** | Enable this checkbox to make Unity apply a compatible format to the render texture if the defined **Color Format** is not supported by the platform.  
**Color Format** | The color format of the render texture.  
**Depth Buffer** | The format of the depth buffer. You can select **No depth buffer** , **At least 16 bits depth (no stencil)** , or **At least 24 bits depth (with stencil)**. The **stencil buffer** is a general purpose buffer that allows you to store an additional unsigned 8-bit integer (0–255) for each pixel drawn to the screen.  
**Mipmap** | Check this box to make the render texture generate a [mipmap](https://docs.unity3d.com/Manual/ImportingTextures.html#Mipmaps).  
**Auto-generate** | Check this box to automatically fill the generated [mipmap](texture-mipmaps-introduction.html) with relevant data. If you don’t enable this, you’ll have to use the [`GenerateMips`](https://docs.unity3d.com/ScriptReference/RenderTexture.GenerateMips.html) function to fill the mipmap levels of that mipmap manually. Alternatively, choose which mipmap level to render into when you call the various `SetRenderTarget` functions. For more information about the `SetRenderTarget` functions, see [`Graphics.SetRenderTarget`](https://docs.unity3d.com/ScriptReference/Graphics.SetRenderTarget.html) and [`Rendering.CommandBuffer.SetRenderTarget`](https://docs.unity3d.com/ScriptReference/Rendering.CommandBuffer.SetRenderTarget.html).  
**Dynamic Scaling** | Check this box to let [dynamic resolution scaling](DynamicResolution-landing.html) resize the render texture. If you don’t enable this, the render texture maintains the same size regardless of the **Dynamic Resolution** A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](DynamicResolution-landing.html)  
See in [Glossary](Glossary.html#dynamicresolution) setting.  
**Wrap Mode** | Controls how the texture is wrapped:  
| **Repeat** | Tiles the texture to create a repeating pattern.  
| **Clamp** | Stretches the edges of the texture. This is useful for preventing wrapping artifacts when you map an image onto an object and you don’t want the texture to tile.  
| **Mirror** | Tiles the texture to create a repeating pattern that mirrors the texture at every integer boundary.  
| **Mirror Once** | Mirrors the texture once, and then falls back to clamping.  
| **Per-axis** | Lets you set different wrap modes for the **U axis** and the **V axis**. The available options are also **Repeat** , **Clamp** , **Mirror** and **Mirror Once**. For example, when you use latitude-longitude environment maps for **reflection probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe), it is useful to have
**Clamp** on the vertical coordinate (**V axis**), but **Repeat** on the
horizontal coordinate (**U axis**).  
**Filter Mode** | Controls how the sampling of the texture uses nearby pixels. The options are:  
| **Point** | Uses the nearest pixel. This makes the texture appear pixelated.  
| **Bilinear** | Uses a weighted average of the four nearest texels. This makes the texture appear blurry when you magnify it.  
| **Trilinear** | Uses a weighted average of the two nearest mipmap levels, which are bilinearly filtered. This creates a soft transition between mipmap levels, at the cost of a slightly more blurry appearance.  
**Aniso Level** The anisotropic filtering (AF) level of a texture. Allows you
to increase texture quality when viewing a texture at a steep angle. Good for
floor and ground textures. [More info](class-TextureImporter.html)  
See in [Glossary](Glossary.html#AnisoLevel) | Anisotropic filtering level of the texture. This increases texture quality when you view the texture at a steep angle. Good for floor, ground, or road textures.  
  
[](class-MovieTexture.html)

Movie Texture Inspector window reference

[](class-CustomRenderTexture.html)

Custom Render Texture Inspector window reference

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

