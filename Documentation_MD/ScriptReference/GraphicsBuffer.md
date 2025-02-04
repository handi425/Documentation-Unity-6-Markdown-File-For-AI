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

# GraphicsBuffer

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

GPU graphics data buffer, for working with geometry or compute shader data.

[ComputeShader](ComputeShader.html) programs often need to read or write
arbitrary data from or to memory buffers, and some rendering algorithms need a
lower level access or control over geometry data than what is provided by the
[Mesh](Mesh.html) class. You can use `GraphicsBuffer` for these cases. You
create the buffers from C# scripts, and then fill them with data using either
C# scripts or compute shader programs.  
  
A graphics buffer is similar to an array in C#, in that it has a number of
elements ([count](GraphicsBuffer-count.html)) of the same size
([stride](GraphicsBuffer-stride.html)). You must supply the intended buffer
usage ([target](GraphicsBuffer-target.html)) when you create a GraphicsBuffer;
for example, you must pass
[GraphicsBuffer.Target.Index](GraphicsBuffer.Target.Index.html) for the buffer
to be usable as a geometry index buffer.  
  
When you have finished working with the buffer, you must manually release the
GPU memory. You can do this using C# dispose pattern, or by calling
[Release](GraphicsBuffer.Release.html).  
  
Additional resources:
[Graphics.RenderPrimitivesIndexed](Graphics.RenderPrimitivesIndexed.html),
[Graphics.RenderPrimitivesIndexedIndirect](Graphics.RenderPrimitivesIndexedIndirect.html),
[Graphics.CopyBuffer](Graphics.CopyBuffer.html),
[ComputeShader](ComputeShader.html),
[Shader.SetGlobalBuffer](Shader.SetGlobalBuffer.html),
[Material.SetBuffer](Material.SetBuffer.html).

### Properties

[bufferHandle](GraphicsBuffer-bufferHandle.html)| The internal handle of this
GraphicsBuffer. Only valid until the buffer is disposed of. (Read Only)  
---|---  
[count](GraphicsBuffer-count.html)| Number of elements in the buffer (Read
Only).  
[name](GraphicsBuffer-name.html)| The debug label for the graphics buffer
(setter only).  
[stride](GraphicsBuffer-stride.html)| Size of one element in the buffer. For
index buffers, this must be either 2 or 4 bytes (Read Only).  
[target](GraphicsBuffer-target.html)| Target, which specifies the intended
target(s) of this GraphicsBuffer (Read Only).  
[usageFlags](GraphicsBuffer-usageFlags.html)| The flags that specify how this
GraphicsBuffer can be used or updated (Read Only).  
  
### Constructors

[GraphicsBuffer](GraphicsBuffer-ctor.html)| Create a Graphics Buffer.  
---|---  
  
### Public Methods

[GetData](GraphicsBuffer.GetData.html)| Read data values from the buffer into
an array. The array can only use blittable types.  
---|---  
[GetNativeBufferPtr](GraphicsBuffer.GetNativeBufferPtr.html)| Retrieve a
native (underlying graphics API) pointer to the buffer.  
[IsValid](GraphicsBuffer.IsValid.html)| Returns true if this graphics buffer
is valid, or false otherwise.  
[LockBufferForWrite](GraphicsBuffer.LockBufferForWrite.html)| Begins a write
operation to the buffer  
[Release](GraphicsBuffer.Release.html)| Release a Graphics Buffer.  
[SetCounterValue](GraphicsBuffer.SetCounterValue.html)| Sets counter value of
append/consume buffer.  
[SetData](GraphicsBuffer.SetData.html)| Set the buffer with values from an
array.  
[UnlockBufferAfterWrite](GraphicsBuffer.UnlockBufferAfterWrite.html)| Ends a
write operation to the buffer  
  
### Static Methods

[CopyCount](GraphicsBuffer.CopyCount.html)| Copy the counter value of a
GraphicsBuffer into another buffer.  
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

