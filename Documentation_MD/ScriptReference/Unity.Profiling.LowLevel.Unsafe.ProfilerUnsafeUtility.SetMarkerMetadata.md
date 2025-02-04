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

#
[ProfilerUnsafeUtility](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.html).SetMarkerMetadata

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

public static void SetMarkerMetadata(IntPtr markerPtr, int index, string name,
byte type, byte unit);

## Declaration

public static void SetMarkerMetadata(IntPtr markerPtr, int index, char* name,
int nameLen, byte type, byte unit);

### Parameters

markerPtr | Profiler marker handle.  
---|---  
index | Metadata parameter index.  
name | Metadata parameter name.  
type | Metadata type. Must be one of ProfilerMarkerDataType values.  
unit | Metadata unit. Must be one of ProfilerMarkerDataUnit values.  
nameLen | Metadata parameter name length.  
  
### Description

Set Profiler marker metadata name and type.

Use to add additional usage context to the Profiler sample metadata parameter.

    
    
    using Unity.Collections.LowLevel.Unsafe;
    using Unity.Profiling;
    using Unity.Profiling.LowLevel;
    using Unity.Profiling.LowLevel.Unsafe;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    class Example
    {
        static IntPtr MakeMarkerWithIntMetadata(string name, string paramName)
        {
            var handle = [ProfilerUnsafeUtility.CreateMarker](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateMarker.html)(name, [ProfilerUnsafeUtility.CategoryScripts](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryScripts.html), [MarkerFlags.Default](Unity.Profiling.LowLevel.MarkerFlags.Default.html), 1);
            [ProfilerUnsafeUtility.SetMarkerMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.SetMarkerMetadata.html)(handle, 0, paramName, (byte)[ProfilerMarkerDataType.Int32](Unity.Profiling.LowLevel.ProfilerMarkerDataType.Int32.html), (byte)[ProfilerMarkerDataUnit.Count](Unity.Profiling.ProfilerMarkerDataUnit.Count.html));
            return handle;
        }  
      
        static readonly IntPtr markerHandle = MakeMarkerWithIntMetadata("MyMarker", "Work Idx");
        static unsafe void DoWork(int num)
        {
            var metadata = stackalloc [ProfilerMarkerData](Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)[1];
            metadata[0].Type = (byte)[ProfilerMarkerDataType.Int32](Unity.Profiling.LowLevel.ProfilerMarkerDataType.Int32.html);
            metadata[0].Size = (uint)[UnsafeUtility.SizeOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<int>();
            metadata[0].Ptr = [UnsafeUtility.AddressOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref num);
            [ProfilerUnsafeUtility.BeginSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(markerHandle, 1, metadata);
            //...
            [ProfilerUnsafeUtility.EndSample](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.EndSample.html)(markerHandle);
        }
    }
    

Additional resources:
[ProfilerMarkerDataType](Unity.Profiling.LowLevel.ProfilerMarkerDataType.html),
[ProfilerMarkerDataUnit](Unity.Profiling.ProfilerMarkerDataUnit.html).

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

