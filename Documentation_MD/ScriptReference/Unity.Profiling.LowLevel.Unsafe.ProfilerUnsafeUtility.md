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

# ProfilerUnsafeUtility

class in Unity.Profiling.LowLevel.Unsafe

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

Utility class which provides access to low level Profiler API.

Use _ProfilerUnsafeUtility_ methods to build a high-level profiling primitive.  
The low level Profiler API is included in a Release Build.

### Static Properties

[CategoryAi](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryAi.html)|
AI and NavMesh Profiler category.  
---|---  
[CategoryAllocation](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryAllocation.html)|
Memory allocation Profiler category.  
[CategoryAnimation](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryAnimation.html)|
Animation Profiler category.  
[CategoryAudio](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryAudio.html)|
Audio system Profiler category.  
[CategoryFileIO](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryFileIO.html)|
File IO Profiler category.  
[CategoryGUI](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryGUI.html)|
UI Profiler category.  
[CategoryInput](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryInput.html)|
Input system Profiler category.  
[CategoryInternal](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryInternal.html)|
Internal Unity systems Profiler category.  
[CategoryLighting](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryLighting.html)|
Global Illumination Profiler category.  
[CategoryLoading](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryLoading.html)|
Loading system Profiler category.  
[CategoryNetwork](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryNetwork.html)|
Networking system Profiler category.  
[CategoryOther](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryOther.html)|
Uncategorized Profiler category.  
[CategoryParticles](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryParticles.html)|
Particle system Profiler category.  
[CategoryPhysics](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryPhysics.html)|
Physics system Profiler category.  
[CategoryPhysics2D](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryPhysics2D.html)|
Physics 2D system Profiler category.  
[CategoryRender](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryRender.html)|
Rendering system Profiler category.  
[CategoryScripts](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryScripts.html)|
Generic C# code Profiler category.  
[CategoryVideo](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryVideo.html)|
Video system Profiler category.  
[CategoryVirtualTexturing](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryVirtualTexturing.html)|
Virtual Texturing system Profiler category.  
[CategoryVr](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryVr.html)|
VR systen Profiler category.  
[Timestamp](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.Timestamp.html)|
Gets Profiler timestamp.  
[TimestampToNanosecondsConversionRatio](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.TimestampToNanosecondsConversionRatio.html)|
Gets conversion ratio from Profiler timestamp to nanoseconds.  
  
### Static Methods

[BeginSample](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSample.html)|
Starts profiling a piece of code marked with a custom name that the markerPtr
handle has defined.  
---|---  
[BeginSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)|
Starts profiling a piece of code marked with a custom name that the markerPtr
handle and metadata parameters has defined.  
[CreateFlow](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateFlow.html)|
Create a new Profiler flow identifier.  
[CreateMarker](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateMarker.html)|
Constructs a new Profiler marker handle for code instrumentation.  
[EndSample](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.EndSample.html)|
End profiling a piece of code marked with a custom name defined by this
instance of ProfilerMarker.  
[FlowEvent](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.FlowEvent.html)|
Add flow event to a Profiler sample.  
[GetCategoryByName](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.GetCategoryByName.html)|
Gets the Profiler category identifier.  
[GetCategoryDescription](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.GetCategoryDescription.html)|
Retrieves Profiler category information such as name or color.  
[SetMarkerMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.SetMarkerMetadata.html)|
Set Profiler marker metadata name and type.  
[SingleSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.SingleSampleWithMetadata.html)|
Creates profiling sample with a custom name that the markerPtr handle and
metadata parameters has defined.  
  
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

