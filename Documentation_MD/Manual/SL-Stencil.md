[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/SL-Stencil.html)
  * [中文](/cn/current/Manual/SL-Stencil.html)
  * [日本語](/ja/current/Manual/SL-Stencil.html)
  * [한국어](/kr/current/Manual/SL-Stencil.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/SL-Stencil.html)
  * [中文](/cn/current/Manual/SL-Stencil.html)
  * [日本語](/ja/current/Manual/SL-Stencil.html)
  * [한국어](/kr/current/Manual/SL-Stencil.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Shader languages reference](shaders-reference.html)
  * [ShaderLab language reference](SL-Reference.html)
  * [GPU render state commands in ShaderLab reference](SL-Commands.html)
  * Stencil command in ShaderLab reference

[](SL-Offset.html)

Offset command in ShaderLab reference

[](SL-ZClip.html)

ZClip command in ShaderLab reference

# Stencil command in ShaderLab reference

Configures settings relating to the **stencil buffer** A memory store that
holds an 8-bit per-pixel value. In Unity, you can use a stencil buffer to flag
pixels, and then only render to pixels that pass the stencil operation. [More
info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#stencilbuffer) on the GPU.

## Render pipeline compatibility

**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Stencil** | Yes | Yes | Yes | Yes  
  
## Syntax

**Signature** | **Example syntax** | **Function**  
---|---|---  
`Stencil`  
`{`  
`Ref <ref>`  
`ReadMask <readMask>`  
`WriteMask <writeMask>`  
`Comp <comparisonOperation>`  
`Pass <passOperation>`  
`Fail <failOperation>`  
`ZFail <zFailOperation>`  
`CompBack <comparisonOperationBack>`  
`PassBack <passOperationBack>`  
`FailBack <failOperationBack>`  
`ZFailBack <zFailOperationBack>`  
`CompFront <comparisonOperationFront>`  
`PassFront <passOperationFront>`  
`FailFront <failOperationFront>`  
`ZFailFront <zFailOperationFront>`  
`}`  
  
Note that all parameters are optional. |  `Stencil`  
`{`  
`Ref 2`  
`Comp equal`  
`Pass keep`  
`ZFail decrWrap`  
`}` | Configures the stencil buffer according to the given parameters.  
  
## Parameters

**Parameter** | **Value** | **Function**  
---|---|---  
**ref** | An integer. Range 0 through 255. Default is 0. | The reference value.  
  
The GPU compares the current contents of the stencil buffer against this
value, using the operation defined in comparisonOperation.  
  
This value is masked with readMask or writeMask, depending on whether a read
or a write operation is occurring.  
  
The GPU can also write this value to the stencil buffer, if Pass, Fail or
ZFail have a value of Replace.  
**readMask** | An integer. Range 0 through 255. Default is 255. | The GPU uses this value as a mask when it performs the stencil test.  
  
See above for the stencil test equation.  
**writeMask** | An integer. Range 0 through 255. Default is 255. | The GPU uses this value as a mask when it writes to the stencil buffer.  
  
Note that, like other masks, it specifies which bits are included in the
operation. For example, a value of 0 means that no bits are included in the
write operation, not that the stencil buffer receives a value of 0.  
**comparisonOperation** | A comparison operation. See Comparison operation values for valid values. Default is Always. | The operation that the GPU performs for the stencil test for all pixels.  
  
This defines the operation for all pixels, regardless of facing. If this is
defined in addition to comparisonOperationBack and comparisonOperationFront,
this value overrides them.  
**passOperation** | A stencil operation. See Stencil operation values for valid values. Default is Keep. | The operation that the GPU performs on the stencil buffer when a pixel pases both the stencil test and the depth test.  
  
This defines the operation for all pixels, regardless of facing. If this is
defined in addition to passOperationBack and passOperationFront, this value
overrides them.  
**failOperation** | A stencil operation. See Stencil operation values for valid values. Default is Keep. | The operation that the GPU performs on the stencil buffer when a pixel fails the stencil test.  
  
This defines the operation for all pixels, regardless of facing. If this is
defined in addition to failOperationBack and failOperationFront, this value
overrides them.  
**zFailOperation** | A stencil operation. See Stencil operation values for valid values. Default is Keep. | The operation that the GPU performs on the stencil buffer when a pixel passes the stencil test, but fails the depth test.  
  
This defines the operation for all pixels, regardless of facing. If this is
defined in addition to zFailOperationBack and zFailOperationFront, this value
overrides them.  
**comparisonOperationBack** | A comparison operation. See Comparison operation values for valid values. Default is Always. | The operation that the GPU performs for the stencil test.  
  
This defines the operation for back-facing pixels only. If comparisonOperation
is defined, that value overrides this one.  
**passOperationBack** | A stencil operation. See Stencil operation values for valid values. Default is Keep. | The operation that the GPU performs on the stencil buffer when a pixel pases both the stencil test and the depth test.  
  
This defines the operation for back-facing pixels only. If passOperation is
defined, that value overrides this one.  
**failOperationBack** | A stencil operation. See Stencil operation values for valid values. Default is Keep. | The operation that the GPU performs on the stencil buffer when a pixel fails the stencil test.  
  
This defines the operation for back-facing pixels only. If failOperation is
defined, that value overrides this one.  
**zFailOperationBack** | A stencil operation. See Stencil operation values for valid values. Default is Keep. | The operation that the GPU performs on the stencil buffer when a pixel passes the stencil test, but fails the depth test.  
  
This defines the operation for back-facing pixels only. If zFailOperation is
defined, that value overrides this one.  
**comparisonOperationFront** | A comparison operation. See Comparison operation values for valid values. Default is Always. | The operation that the GPU performs for the stencil test.  
  
This defines the operation for front-facing pixels only. If
comparisonOperation is defined, that value overrides this one.  
**passOperationFront** | A stencil operation. See Stencil operation values for valid values. Default is Keep. | The operation that the GPU performs on the stencil buffer when a pixel pases both the stencil test and the depth test.  
  
This defines the operation for front-facing pixels only. If passOperation is
defined, that value overrides this one.  
**failOperationFront** | A stencil operation. See Stencil operation values for valid values. Default is Keep. | The operation that the GPU performs on the stencil buffer when a pixel fails the stencil test.  
  
This defines the operation for front-facing pixels only. If failOperation is
defined, that value overrides this one.  
**zFailOperationFront** | A stencil operation. See Stencil operation values for valid values. Default is Keep. | The operation that the GPU performs on the stencil buffer when a pixel passes the stencil test, but fails the depth test.  
  
This defines the operation for front-facing pixels only. If zFailOperation is
defined, that value overrides this one.  
  
### Comparison values

In C#, these values are represented by the
[Rendering.CompareFunction](../ScriptReference/Rendering.CompareFunction.html)
enum.

**Value** | **Corresponding integer value in Rendering.CompareFunction enum** | **Function**  
---|---|---  
`Never` | 1 | Never render **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel).  
`Less` | 2 | Render pixels when their reference value is less than the current value in the stencil buffer.  
`Equal` | 3 | Render pixels when their reference value is equal to the current value in the stencil buffer.  
`LEqual` | 4 | Render pixels when their reference value is less than or equal to the current value in the stencil buffer.  
`Greater` | 5 | Render pixels when their reference value is greater than the current value in the stencil buffer.  
`NotEqual` | 6 | Render pixels when their reference value differs from the current value in the stencil buffer.  
`GEqual` | 7 | Render pixels when their reference value is greater than or equal to the current value in the stencil buffer.  
`Always` | 8 | Always render pixels.  
  
### Stencil values

In C#, these values are represented by the
[Rendering.Rendering.StencilOp](../ScriptReference/Rendering.StencilOp.html)
enum.

**Value** | **Corresponding integer value in Rendering.StencilOp enum** | **Function**  
---|---|---  
`Keep` | 0 | Keep the current contents of the stencil buffer.  
`Zero` | 1 | Write 0 into the stencil buffer.  
`Replace` | 2 | Write the reference value into the buffer.  
`IncrSat` | 3 | Increment the current value in the buffer. If the value is 255 already, it stays at 255.  
`DecrSat` | 4 | Decrement the current value in the buffer. If the value is 0 already, it stays at 0.  
`Invert` | 5 | Negate all the bits of the current value in the buffer.  
`IncrWrap` | 6 | Increment the current value in the buffer. If the value is 255 already, it becomes 0.  
`DecrWrap` | 7 | Decrement the current value in the buffer. If the value is 0 already, it becomes 255.  
  
## Additional resources

  * [Check or write to the stencil buffer in a shader](writing-shader-set-stencil.html)

[](SL-Offset.html)

Offset command in ShaderLab reference

[](SL-ZClip.html)

ZClip command in ShaderLab reference

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

