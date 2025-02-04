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

# AsyncReadManagerRequestMetric

struct in Unity.IO.LowLevel.Unsafe

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

Metrics for an individual read request.

Get metrics records by calling AsyncReadManager.GetMetrics.

### Properties

[AssetName](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.AssetName.html)|
The name of the asset being read.  
---|---  
[AssetTypeId](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.AssetTypeId.html)|
The type ID of the asset being read in the read request.  
[BatchReadCount](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.BatchReadCount.html)|
The number of batch read commands contained in the read request.  
[CurrentBytesRead](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.CurrentBytesRead.html)|
Total number of bytes of the read request read so far.  
[FileName](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.FileName.html)|
The filename the read request is reading from.  
[IsBatchRead](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.IsBatchRead.html)|
Returns whether this read request contained batch read commands.  
[OffsetBytes](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.OffsetBytes.html)|
The offset of the read request from the start of the file, in bytes.  
[PriorityLevel](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.PriorityLevel.html)|
The priority level of the read request.  
[ReadType](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.ReadType.html)|
The read type (sync or async) of the read request.  
[RequestTimeMicroseconds](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.RequestTimeMicroseconds.html)|
The time at which the read request was made, in microseconds elapsed since
application startup.  
[SizeBytes](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.SizeBytes.html)|
The size of the read request, in bytes.  
[State](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.State.html)|
The state of the read request at the time of retrieving the metrics.  
[Subsystem](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.Subsystem.html)|
The Subsystem tag assigned to the read operation.  
[TimeInQueueMicroseconds](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.TimeInQueueMicroseconds.html)|
The amount of time the read request waited in the AsyncReadManager queue, in
microseconds.  
[TotalTimeMicroseconds](Unity.IO.LowLevel.Unsafe.AsyncReadManagerRequestMetric.TotalTimeMicroseconds.html)|
The total time in microseconds from the read request being added until its
completion, or the time of metrics retrieval, depending whether the read has
completed or not.  
  
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

