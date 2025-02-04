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

# Profiler

class in UnityEngine.Profiling

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

Controls the [Profiler](../Manual/Profiler.html) from script.

You can add custom Profiler sections in your scripts with
[Profiler.BeginSample](Profiling.Profiler.BeginSample.html) and
[Profiler.EndSample](Profiling.Profiler.EndSample.html).  
  
On standalone platforms, you can save all profiling information to a file,
which allows you to inspect it later. To do this, you must specify a
[Profiler.logFile](Profiling.Profiler-logFile.html) and set both
[Profiler.enabled](Profiling.Profiler-enabled.html) and
[Profiler.enableBinaryLog](Profiling.Profiler-enableBinaryLog.html) to `true`.  
  
Because use of the Profiler negatively affects the performance of your app,
most of the Profiler API functionality is only available when you enable the
`Development Build`. Therefore, you must enable `Developer Build` if you want
to use profiler API methods in your built app. Disabling `Development Build`
makes your app run faster, but prevents you from using most of the Profiler
API methods.  
  
The exception to this are the Profiler API methods relating to memory usage.
Because Unity manages most of its system memory at run-time, it can provide
that information with no performance penalty; therefore these methods are
available even if you don't enable `Development Build`. This applies to all
memory-related Profiler API methods except
[Profiler.GetAllocatedMemoryForGraphicsDriver](Profiling.Profiler.GetAllocatedMemoryForGraphicsDriver.html)
and
[Profiler.GetRuntimeMemorySizeLong](Profiling.Profiler.GetRuntimeMemorySizeLong.html),
since they require extra profiling data only available in development builds.

### Static Properties

[areaCount](Profiling.Profiler-areaCount.html)| The number of Profiler Areas
that you can profile.  
---|---  
[enableAllocationCallstacks](Profiling.Profiler-
enableAllocationCallstacks.html)| Enables the recording of callstacks for
managed allocations.  
[enableBinaryLog](Profiling.Profiler-enableBinaryLog.html)| Enables the
logging of profiling data to a file.  
[enabled](Profiling.Profiler-enabled.html)| Enables the Profiler.  
[logFile](Profiling.Profiler-logFile.html)| Specifies the file to use when
writing profiling data.  
[maxUsedMemory](Profiling.Profiler-maxUsedMemory.html)| Sets the maximum
amount of memory that Profiler uses for buffering data. This property is
expressed in bytes.  
[usedHeapSizeLong](Profiling.Profiler-usedHeapSizeLong.html)| Returns the
number of bytes that Unity has allocated. This does not include bytes
allocated by external libraries or drivers.  
  
### Static Methods

[AddFramesFromFile](Profiling.Profiler.AddFramesFromFile.html)| Displays the
recorded profile data in the profiler.  
---|---  
[BeginSample](Profiling.Profiler.BeginSample.html)| Begin profiling a piece of
code with a custom label.  
[BeginThreadProfiling](Profiling.Profiler.BeginThreadProfiling.html)| Enables
profiling on the thread from which you call this method.  
[EmitFrameMetaData](Profiling.Profiler.EmitFrameMetaData.html)| Write metadata
associated with the current frame to the Profiler stream.  
[EmitSessionMetaData](Profiling.Profiler.EmitSessionMetaData.html)| Write
metadata associated with the whole Profiler session capture.  
[EndSample](Profiling.Profiler.EndSample.html)| Ends the current profiling
sample.  
[EndThreadProfiling](Profiling.Profiler.EndThreadProfiling.html)| Frees the
internal resources used by the Profiler for the thread.  
[GetAllCategories](Profiling.Profiler.GetAllCategories.html)| Returns all
ProfilerCategory registered in Profiler.  
[GetAllocatedMemoryForGraphicsDriver](Profiling.Profiler.GetAllocatedMemoryForGraphicsDriver.html)|
Returns the amount of allocated memory for the graphics driver, in bytes.Only
available in development players and editor.  
[GetAreaEnabled](Profiling.Profiler.GetAreaEnabled.html)| Returns whether or
not a given ProfilerArea is currently enabled.  
[GetCategoriesCount](Profiling.Profiler.GetCategoriesCount.html)| Returns
number of ProfilerCategory registered in Profiler.  
[GetMonoHeapSizeLong](Profiling.Profiler.GetMonoHeapSizeLong.html)| Returns
the size of the reserved space for managed-memory.  
[GetMonoUsedSizeLong](Profiling.Profiler.GetMonoUsedSizeLong.html)| Gets the
allocated managed memory for live objects and non-collected objects.  
[GetRuntimeMemorySizeLong](Profiling.Profiler.GetRuntimeMemorySizeLong.html)|
Gathers the native-memory used by a Unity object.  
[GetTempAllocatorSize](Profiling.Profiler.GetTempAllocatorSize.html)| Returns
the size of the temp allocator.  
[GetTotalAllocatedMemoryLong](Profiling.Profiler.GetTotalAllocatedMemoryLong.html)|
The total memory allocated by the internal allocators in Unity. Unity reserves
large pools of memory from the system; this includes double the required
memory for textures because Unity keeps a copy of each texture on both the CPU
and GPU. This function returns the amount of used memory in those pools.  
[GetTotalFragmentationInfo](Profiling.Profiler.GetTotalFragmentationInfo.html)|
Returns heap memory fragmentation information.  
[GetTotalReservedMemoryLong](Profiling.Profiler.GetTotalReservedMemoryLong.html)|
The total memory Unity has reserved.  
[GetTotalUnusedReservedMemoryLong](Profiling.Profiler.GetTotalUnusedReservedMemoryLong.html)|
Unity allocates memory in pools for usage when unity needs to allocate memory.
This function returns the amount of unused memory in these pools.  
[IsCategoryEnabled](Profiling.Profiler.IsCategoryEnabled.html)| Returns
whether or not a given ProfilerCategory is currently enabled.  
[SetAreaEnabled](Profiling.Profiler.SetAreaEnabled.html)| Enable or disable a
given ProfilerArea.  
[SetCategoryEnabled](Profiling.Profiler.SetCategoryEnabled.html)| Enable or
disable a given ProfilerCategory.  
[SetTempAllocatorRequestedSize](Profiling.Profiler.SetTempAllocatorRequestedSize.html)|
Sets the size of the temp allocator.  
  
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

