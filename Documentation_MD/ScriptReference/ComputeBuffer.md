[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# ComputeBuffer

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

GPU data buffer, mostly for use with compute shaders.

[ComputeShader](ComputeShader.html) programs often need arbitrary data to be
read & written into memory buffers. ComputeBuffer class is exactly for that -
you can create & fill them from script code, and use them in compute shaders
or regular shaders.  
  
Compute buffers are always supported in compute shaders. Compute shader
support can be queried runtime using
[SystemInfo.supportsComputeShaders](SystemInfo-supportsComputeShaders.html).
See the [Compute Shaders](../Manual/class-ComputeShader.html) Manual page for
more information about platforms supporting compute shaders. In regular
graphics shaders the compute buffer support requires minimum [shader model
4.5](../Manual/SL-ShaderCompileTargets.html).  
  
For a ComputeBuffer that uses a counter, Metal and Vulkan platforms don't have
native counters and use separate small buffers that act as counters
internally. These small buffers are bound separately from the ComputeBuffer
and count towards the limit of possible buffers bound (31 for Metal, based on
the device for Vulkan).  
  
On the shader side, ComputeBuffers with default
[ComputeBufferType](ComputeBufferType.html) map to `StructuredBuffer<T>` and
`RWStructuredBuffer<T>` in HLSL.  
  
Additional resources: [ComputeShader](ComputeShader.html) class,
[Shader.SetGlobalBuffer](Shader.SetGlobalBuffer.html),
[Material.SetBuffer](Material.SetBuffer.html), [Compute
Shaders](../Manual/class-ComputeShader.html) overview.

### Properties

[count](ComputeBuffer-count.html)| Number of elements in the buffer (Read
Only).  
---|---  
[name](ComputeBuffer-name.html)| The debug label for the compute buffer
(setter only).  
[stride](ComputeBuffer-stride.html)| Size of one element in the buffer in
bytes (Read Only).  
  
### Constructors

[ComputeBuffer](ComputeBuffer-ctor.html)| Create a Compute Buffer.  
---|---  
  
### Public Methods

[BeginWrite](ComputeBuffer.BeginWrite.html)| Begins a write operation to the
buffer  
---|---  
[EndWrite](ComputeBuffer.EndWrite.html)| Ends a write operation to the buffer  
[GetData](ComputeBuffer.GetData.html)| Read data values from the buffer into
an array. The array can only use blittable types.  
[GetNativeBufferPtr](ComputeBuffer.GetNativeBufferPtr.html)| Retrieve a native
(underlying graphics API) pointer to the buffer.  
[IsValid](ComputeBuffer.IsValid.html)| Returns true if this compute buffer is
valid and false otherwise.  
[Release](ComputeBuffer.Release.html)| Release a Compute Buffer.  
[SetCounterValue](ComputeBuffer.SetCounterValue.html)| Sets counter value of
append/consume buffer.  
[SetData](ComputeBuffer.SetData.html)| Set the buffer with values from an
array.  
  
### Static Methods

[CopyCount](ComputeBuffer.CopyCount.html)| Copy counter value of
append/consume buffer into another buffer.  
---|---  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

