[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/urp/urp-shaders/fullscreen-master-stack-reference.html)
  * [中文](/cn/current/Manual/urp/urp-shaders/fullscreen-master-stack-reference.html)
  * [日本語](/ja/current/Manual/urp/urp-shaders/fullscreen-master-stack-reference.html)
  * [한국어](/kr/current/Manual/urp/urp-shaders/fullscreen-master-stack-reference.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/urp/urp-shaders/fullscreen-master-stack-reference.html)
  * [中文](/cn/current/Manual/urp/urp-shaders/fullscreen-master-stack-reference.html)
  * [日本語](/ja/current/Manual/urp/urp-shaders/fullscreen-master-stack-reference.html)
  * [한국어](/kr/current/Manual/urp/urp-shaders/fullscreen-master-stack-reference.html)

  * [Rendering](../../rendering-and-post-processing.html)
  * [Post-processing and full-screen effects](../../post-processing-and-full-screen-effects.html)
  * [Post-processing and full-screen effects in URP](../../urp/post-processing-and-full-screen-effects-urp.html)
  * [Post-processing in URP](../../urp/post-processing-in-urp.html)
  * [Custom post-processing in URP](../../urp/post-processing/custom-post-processing.html)
  * [Creating a full-screen shader in Shader Graph in URP](../../urp/urp-shaders/fullscreen-master-stack-urp.html)
  * Fullscreen Master Stack in Shader Graph reference for URP

[](../../urp/urp-shaders/fullscreen-master-stack-shader-graph.html)

Fullscreen Master Stack reference for Shader Graph in URP

[](../../graphics-color.html)

Color

# Fullscreen Master Stack in Shader Graph reference for URP

The Fullscreen Master Stack has a variety of properties in the Graph Settings
window which control the overall appearance of the Fullscreen **shader** A
program that runs on the GPU. [More info](../../Shaders.html)  
See in [Glossary](../../Glossary.html#Shader).

##  Surface Options

**Property** | **Description**  
---|---  
**Allow Override Material** | Exposes the Graph Settings properties in the Material’s **Surface Options**. **Note:** You can only expose properties that you enable in **Graph Settings.** If you enable one of these properties, you can’t disable it in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](../../UsingTheInspector.html)  
See in [Glossary](../../Glossary.html#Inspector) under the Material’s
**Surface Options.**  
**Blend Mode** | Specifies the blend mode to use when Unity renders the full-screen shader. Each option has an equivalent [`BlendMode`](https://docs.unity3d.com/ScriptReference/Rendering.BlendMode.html) operation. **Note** : When you write to a **Blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](../../Glossary.html#blit) shader, disable this property to
avoid undesired effects.  
**Alpha** | Uses the shader’s alpha value to control its opacity. `BlendMode` operation: `Blend SrcAlpha OneMinusSrcAlpha`  
**Premultiply** | Multiplies the RGB values of the transparent shader by its alpha value, then applies a similar effect to the shader as **Alpha**. `BlendMode` operation: `Blend One OneMinusSrcAlpha`  
**Additive** | Adds the color values of the full-screen shader and the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](../../CamerasOverview.html)  
See in [Glossary](../../Glossary.html#Camera) output together. `BlendMode`
operation: `Blend One One`  
**Multiply** | Multiplies the color of the full-screen shader with the color of the Camera’s output. `BlendMode` operation: `Blend DstColor Zero`  
**Custom** | Set every parameter of the blending equation manually. For more information, refer to Custom blend modes.  
**Depth Test** | Specifies the function this shader uses to perform the depth test.  
**Disabled** | Does not perform a depth test.  
**Never** | The depth test never passes.  
**Less** | The depth test passes if the **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](../../ShadowPerformance.html)  
See in [Glossary](../../Glossary.html#pixel)’s depth value is less than the
value stored in the **depth buffer** A memory store that holds the z-value
depth of each pixel in an image, where the z-value is the depth for each
rendered pixel from the projection plane. [More info](../../class-
RenderTexture.html)  
See in [Glossary](../../Glossary.html#depthbuffer).  
**Equal** | The depth test passes if the pixel’s depth value is equal to the value stored in the depth buffer.  
**Less Equal** | The depth test passes if the pixel’s depth value is less than or equal to the value stored in the depth buffer. This renders the tested pixel in front of other pixels.  
**Greater** | The depth test passes if the pixel’s depth value is greater than the value stored in the depth buffer.  
**Not Equal** | The depth test passes if the pixel’s depth value is not equal to the value stored in the depth buffer.  
**Greater Equal** | The depth test passes if the pixel’s depth value is greater than or equal to the value stored in the depth buffer.  
**Always** | The depth test always passes, and Unity does not compare the pixel’s depth value to the value it has stored in the depth buffer.  
**Depth Write** | Indicates whether Unity writes depth values for **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](../../class-GameObject.html)  
See in [Glossary](../../Glossary.html#GameObject) that use this shader. Enable
this property to write the depth value to the depth buffer and use a depth
Fragment block.  
**Depth Write Mode** | Determines the depth value’s input format before Unity passes it to the depth buffer. This property determines which Depth block you can use in the Fragment context.This property appears when you enable **Depth Write**.  
**LinearEye** | Converts the depth value into a value scaled to world space. This new value represents the depth (in meters) from the near to the far plane of the Camera.  
**Linear01** | Uses a linear depth value range between 0 and 1.  
**Raw** | Does not convert the depth buffer value. Use this setting with a nonlinear depth value or when you directly sample the depth value from the depth buffer.  
**Enable Stencil** | This property gives you control over all stencil fields. Refer to Stencil properties for information about the options that become available when you enable this property.  
**Custom Editor GUI** | Accepts the full name of a C# class that inherits [`FullscreenShaderGUI`](https://docs.unity3d.com/Packages/com.unity.shadergraph@15.0/api/UnityEditor.Rendering.Fullscreen.ShaderGraph.FullscreenShaderGUI.html). For information on how to use a custom editor, refer to [ShaderLab: assigning a custom editor](https://docs.unity3d.com/2021.2/Documentation/Manual/SL-CustomEditor.html).  
  
##  Custom Blend Mode

Use the **Custom** blend mode to create a blend mode different from those
available in Surface Options. To show these options, set **Blend Mode** to
**Custom**. The Custom blend mode properties specify the blending operation to
use for this full-screen shader’s alpha and color channels.

In the blend mode properties, **Src** (source) refers to the full-screen
shader itself. **Dst** (destination) refers to the **Scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](../../CreatingScenes.html)  
See in [Glossary](../../Glossary.html#Scene) camera’s raw output, which this
shader doesn’t affect. The blending operation applies the source contents to
the destination contents to produce a rendering result.

For more information on the blending equation, refer to [ShaderLab command:
Blend](https://docs.unity3d.com/Manual/SL-Blend.html).

### Color Blend Mode

Determines the blending equation Unity uses for the red, green, and blue
channels (RGB). Each setting defines one part of the equation.

**Property** | **Description**  
---|---  
**Src Color** | Sets the blend mode of the source color.  
**Dst Color** | Sets the blend mode of the destination color.  
**Color Operation** | Determines how to combine the source and destination color during the blending process. For information on these options refer to [ShaderLab command: BlendOp](https://docs.unity3d.com/Manual/SL-BlendOp.html)  
  
### Alpha Blend Mode

Determines the blending equation Unity uses for the alpha channel. Each
setting defines one part of the equation.

**Property** | **Description**  
---|---  
**Src** | Sets the blend mode of the source alpha. For information on these options, refer to [Valid parameter values](https://docs.unity3d.com/Manual/SL-Blend.html#valid-parameter-values).  
**Dst** | Sets the blend mode of the destination alpha. For information on these options, refer to [Valid parameter values](https://docs.unity3d.com/Manual/SL-Blend.html).  
**Blend Operation Alpha** | Determines how to combine the source and destination alpha during the blending process. For more information on these options, refer to [ShaderLab command: BlendOp](https://docs.unity3d.com/Manual/SL-BlendOp.html)  
  
##  Stencil properties

These properties affect how this full-screen Shader Graph uses the **stencil
buffer** A memory store that holds an 8-bit per-pixel value. In Unity, you can
use a stencil buffer to flag pixels, and then only render to pixels that pass
the stencil operation. [More info](../../class-RenderTexture.html)  
See in [Glossary](../../Glossary.html#stencilbuffer). For more information on
the stencil buffer, refer to [SL-Stencil](https://docs.unity3d.com/Manual/SL-
Stencil.html).

**Property** | **Description**  
---|---  
**Reference** | Determines the stencil reference value this shader uses for all stencil operations.  
**Read Mask** | Determines which bits this shader can read during the stencil test.  
**Write Mask** | Determines which bits this shader can write to during the stencil test.  
**Comparison** | Determines the comparison function this shader uses during the stencil test.  
**Disabled** | Does not perform a stencil test.  
**Never** | The stencil test never passes.  
**Less** | The stencil test passes if the pixel’s depth value is less than the value stored in the depth buffer.  
**Equal** | The stencil test passes if the pixel’s depth value is equal to the value stored in the depth buffer.  
**Less Equal** | The stencil test passes if the pixel’s depth value is less than or equal to than the depth buffer value. This renders the tested pixel in front of other pixels.  
**Greater** | The stencil test passes if the pixel’s depth value is greater than the value stored in the depth buffer.  
**Not Equal** | The stencil test passes if the pixel’s depth value is not equal to the value stored in the depth buffer.  
**Greater Equal** | The stencil test passes if the pixel’s depth value is greater than or equal to the value stored in the depth buffer.  
**Always** | The stencil test always passes,and Unity does not compare the pixel’s depth value to the value it has stored in the depth buffer.  
**Pass** | Determines the operation this shader executes if the stencil test succeeds.  
For more information on this property’s options, refer to pass and fail
options.  
**Fail** | Determines the operation this shader executes if the stencil test fails.  
For more information on this property’s options, refer to pass and fail
options.  
**Depth Fail** | Determines the operation this shader executes if the depth test fails. This option has no effect if the depth test **Comparison** value is **Never** or **Disabled.**  
For more information on this property’s options, refer to pass and fail
options.  
  
###  Pass and Fail options

**Option** | **Description**  
---|---  
**Keep** | Does not change the current contents of the stencil buffer.  
**Zero** | Writes a value of 0 into the stencil buffer.  
**Replace** | Writes the **Reference** value into the buffer.  
**IncrementSaturate** | Adds a value of 1 to the current value in the buffer. A value of 255 remains 255.  
**DecrementSaturate** | Subtracts a value of 1 from the current value in the buffer. A value of 0 remains 0.  
**Invert** | Performs a bitwise NOT operation. This means it negates all the bits of the current value in the buffer.  
For example, a decimal value of 59 is 0011 1011 in binary. The NOT operation
reverses each bit to 1100 0100, which is a decimal value of 196.  
**IncrementWrap** | Adds a value of 1 to the current value in the buffer. A value of 255 becomes 0.  
**DecrementWrap** | Subtracts a value of 1 from the current value in the buffer. A value of 0 becomes 255.  
  
[](../../urp/urp-shaders/fullscreen-master-stack-shader-graph.html)

Fullscreen Master Stack reference for Shader Graph in URP

[](../../graphics-color.html)

Color

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

