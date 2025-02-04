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

#  [BatchRendererGroup](Rendering.BatchRendererGroup.html).AddBatch

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

public [Rendering.BatchID](Rendering.BatchID.html)
AddBatch(NativeArray<MetadataValue> batchMetadata,
[GraphicsBufferHandle](GraphicsBufferHandle.html) buffer);

## Declaration

public [Rendering.BatchID](Rendering.BatchID.html)
AddBatch(NativeArray<MetadataValue> batchMetadata,
[GraphicsBufferHandle](GraphicsBufferHandle.html) buffer, uint bufferOffset,
uint windowSize);

### Parameters

batchMetadata | The metadata properties for this batch.  
---|---  
buffer | The `GraphicsBufferHandle` of the `GraphicsBuffer` associated with this batch.  
bufferOffset | The offset amount of the data to bound within the Uniform Buffer Object (UBO). This value defaults to zero, which is the start of the buffer. If this is a constant buffer, this value must be an integer multiple of [BatchRendererGroup.GetConstantBufferOffsetAlignment](Rendering.BatchRendererGroup.GetConstantBufferOffsetAlignment.html).  
windowSize | Amount of data in the buffer to be bound, starting from the bufferOffset value. Defaults to zero. If this is a constant buffer, this value must be less or equal to [BatchRendererGroup.GetConstantBufferMaxWindowSize](Rendering.BatchRendererGroup.GetConstantBufferMaxWindowSize.html).  
  
### Returns

**BatchID** ID of the batch Unity has created.

### Description

Create a draw command batch that shares a single set of metadata values and a
single `GraphicsBuffer`.

Every buffer you pass in to this method must have the correct buffer target
for the active graphics API. Use the BatchRendererGroup.BatchBufferTarget
query to find out which buffer target you should use. If the target is
[BatchBufferTarget.RawBuffer](Rendering.BatchBufferTarget.RawBuffer.html) then
both bufferOffset and windowSize must be zero If the target is
[BatchBufferTarget.ConstantBuffer](Rendering.BatchBufferTarget.ConstantBuffer.html),
then bufferOffset must be an integer multiple of the
[BatchRendererGroup.GetConstantBufferOffsetAlignment](Rendering.BatchRendererGroup.GetConstantBufferOffsetAlignment.html)
value (zero allowed), and windowSize must be less than or equal to the
[BatchRendererGroup.GetConstantBufferMaxWindowSize](Rendering.BatchRendererGroup.GetConstantBufferMaxWindowSize.html)
value. The combined value of bufferOffset and windowSize must be less than or
equal to the size of the ConstantBuffer.

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

