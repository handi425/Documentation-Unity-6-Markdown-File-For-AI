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

#  [ProfilerMarker](Unity.Profiling.ProfilerMarker.html).Handle

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

public IntPtr Handle;

### Description

Gets native handle of the
[ProfilerMarker](Unity.Profiling.ProfilerMarker.ProfilerMarker.html).

Use _Handle_ to obtain a native marker handle and extend funtionality of
[ProfilerMarker](Unity.Profiling.ProfilerMarker.ProfilerMarker.html).

    
    
    using System.Diagnostics;
    using System.Runtime.CompilerServices;
    using Unity.Collections.LowLevel.Unsafe;
    using Unity.Profiling;
    using Unity.Profiling.LowLevel;
    using Unity.Profiling.LowLevel.Unsafe;  
      
    public static class ProfilerMarkerExtension
    {
        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        [Conditional("ENABLE_PROFILER")]
        public static unsafe void Begin(this [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) marker, int metadata)
        {
            var data = new [ProfilerMarkerData](Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)();
            data.Type = (byte)[ProfilerMarkerDataType.Int32](Unity.Profiling.LowLevel.ProfilerMarkerDataType.Int32.html);
            data.Size = (uint)[UnsafeUtility.SizeOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<int>();
            data.Ptr = [UnsafeUtility.AddressOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref metadata);
            [ProfilerUnsafeUtility.BeginSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, &data);
        }  
      
        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        [Conditional("ENABLE_PROFILER")]
        public static unsafe void Begin(this [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) marker, uint metadata)
        {
            var data = new [ProfilerMarkerData](Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)();
            data.Type = (byte)[ProfilerMarkerDataType.UInt32](Unity.Profiling.LowLevel.ProfilerMarkerDataType.UInt32.html);
            data.Size = (uint)[UnsafeUtility.SizeOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<uint>();
            data.Ptr = [UnsafeUtility.AddressOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref metadata);
            [ProfilerUnsafeUtility.BeginSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, &data);
        }  
      
        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        [Conditional("ENABLE_PROFILER")]
        public static unsafe void Begin(this [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) marker, long metadata)
        {
            var data = stackalloc [ProfilerMarkerData](Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)[1];
            data[0].Type = (byte)[ProfilerMarkerDataType.Int64](Unity.Profiling.LowLevel.ProfilerMarkerDataType.Int64.html);
            data[0].Size = (uint)[UnsafeUtility.SizeOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<long>();
            data[0].Ptr = [UnsafeUtility.AddressOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref metadata);
            [ProfilerUnsafeUtility.BeginSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, data);
        }  
      
        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        [Conditional("ENABLE_PROFILER")]
        public static unsafe void Begin(this [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) marker, ulong metadata)
        {
            var data = stackalloc [ProfilerMarkerData](Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)[1];
            data[0].Type = (byte)[ProfilerMarkerDataType.UInt64](Unity.Profiling.LowLevel.ProfilerMarkerDataType.UInt64.html);
            data[0].Size = (uint)[UnsafeUtility.SizeOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<ulong>();
            data[0].Ptr = [UnsafeUtility.AddressOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref metadata);
            [ProfilerUnsafeUtility.BeginSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, data);
        }  
      
        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        [Conditional("ENABLE_PROFILER")]
        public static unsafe void Begin(this [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) marker, float metadata)
        {
            var data = stackalloc [ProfilerMarkerData](Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)[1];
            data[0].Type = (byte)[ProfilerMarkerDataType.Float](Unity.Profiling.LowLevel.ProfilerMarkerDataType.Float.html);
            data[0].Size = (uint)[UnsafeUtility.SizeOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<float>();
            data[0].Ptr = [UnsafeUtility.AddressOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref metadata);
            [ProfilerUnsafeUtility.BeginSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, data);
        }  
      
        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        [Conditional("ENABLE_PROFILER")]
        public static unsafe void Begin(this [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) marker, double metadata)
        {
            var data = stackalloc [ProfilerMarkerData](Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)[1];
            data[0].Type = (byte)[ProfilerMarkerDataType.Double](Unity.Profiling.LowLevel.ProfilerMarkerDataType.Double.html);
            data[0].Size = (uint)[UnsafeUtility.SizeOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.SizeOf.html)<double>();
            data[0].Ptr = [UnsafeUtility.AddressOf](Unity.Collections.LowLevel.Unsafe.UnsafeUtility.AddressOf.html)(ref metadata);
            [ProfilerUnsafeUtility.BeginSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, data);
        }  
      
        [MethodImpl(MethodImplOptions.AggressiveInlining)]
        [Conditional("ENABLE_PROFILER")]
        public static unsafe void Begin(this [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) marker, string metadata)
        {
            var data = stackalloc [ProfilerMarkerData](Unity.Profiling.LowLevel.Unsafe.ProfilerMarkerData.html)[1];
            data[0].Type = (byte)[ProfilerMarkerDataType.String16](Unity.Profiling.LowLevel.ProfilerMarkerDataType.String16.html);
            fixed(char* c = metadata)
            {
                data[0].Size = ((uint)metadata.Length + 1) * 2;
                data[0].Ptr = c;
                [ProfilerUnsafeUtility.BeginSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html)(marker.Handle, 1, data);
            }
        }
    }
    

Additional resources:
[ProfilerUnsafeUtility.CreateMarker](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateMarker.html),
[ProfilerUnsafeUtility.BeginSampleWithMetadata](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSampleWithMetadata.html).

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

