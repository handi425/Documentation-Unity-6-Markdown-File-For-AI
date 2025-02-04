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

#  [CommandBuffer](Rendering.CommandBuffer.html).SetBufferData

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

## Declaration

public void SetBufferData([ComputeBuffer](ComputeBuffer.html) buffer, Array
data);

## Declaration

public void SetBufferData([ComputeBuffer](ComputeBuffer.html) buffer, List<T>
data);

## Declaration

public void SetBufferData([ComputeBuffer](ComputeBuffer.html) buffer,
NativeArray<T> data);

## Declaration

public void SetBufferData([GraphicsBuffer](GraphicsBuffer.html) buffer, Array
data);

## Declaration

public void SetBufferData([GraphicsBuffer](GraphicsBuffer.html) buffer,
List<T> data);

## Declaration

public void SetBufferData([GraphicsBuffer](GraphicsBuffer.html) buffer,
NativeArray<T> data);

### Parameters

buffer | The destination buffer.  
---|---  
data | Array of values to fill the buffer.  
  
### Description

Adds a command to set the buffer with values from an array.

The input data must follow the data layout rules of the graphics API in use.
See [Compute Shaders](../Manual/class-ComputeShader.html) for cross-platform
compatibility information.  
  
Note: Because only [blittable](https://docs.microsoft.com/en-
us/dotnet/framework/interop/blittable-and-non-blittable-types) data types can
be copied from the array to the buffer, the array must only contain elements
of a blittable type. If you attempt to use non-blittable types, an exception
will be raised.

* * *

## Declaration

public void SetBufferData([ComputeBuffer](ComputeBuffer.html) buffer, Array
data, int managedBufferStartIndex, int graphicsBufferStartIndex, int count);

## Declaration

public void SetBufferData([ComputeBuffer](ComputeBuffer.html) buffer,
NativeArray<T> data, int nativeBufferStartIndex, int graphicsBufferStartIndex,
int count);

## Declaration

public void SetBufferData([ComputeBuffer](ComputeBuffer.html) buffer, List<T>
data, int managedBufferStartIndex, int graphicsBufferStartIndex, int count);

## Declaration

public void SetBufferData([GraphicsBuffer](GraphicsBuffer.html) buffer, Array
data, int managedBufferStartIndex, int graphicsBufferStartIndex, int count);

## Declaration

public void SetBufferData([GraphicsBuffer](GraphicsBuffer.html) buffer,
NativeArray<T> data, int nativeBufferStartIndex, int graphicsBufferStartIndex,
int count);

## Declaration

public void SetBufferData([GraphicsBuffer](GraphicsBuffer.html) buffer,
List<T> data, int managedBufferStartIndex, int graphicsBufferStartIndex, int
count);

### Parameters

buffer | The destination buffer.  
---|---  
data | Array of values to fill the buffer.  
managedBufferStartIndex | The first element index in data to copy to the compute buffer.  
graphicsBufferStartIndex | The first element index in compute buffer to receive the data.  
count | The number of elements to copy.  
nativeBufferStartIndex | The first element index in data to copy to the compute buffer.  
  
### Description

Adds a command to process a partial copy of data values from an array into the
buffer.

The input data must follow the data layout rules of the graphics API in use.
See [Compute Shaders](../Manual/class-ComputeShader.html) for cross-platform
compatibility information.  
  
Note: Because only [blittable](https://docs.microsoft.com/en-
us/dotnet/framework/interop/blittable-and-non-blittable-types) data types can
be copied from the array to the buffer, the array must only contain elements
of a blittable type. If you attempt to use non-blittable types, an exception
will be raised.

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

