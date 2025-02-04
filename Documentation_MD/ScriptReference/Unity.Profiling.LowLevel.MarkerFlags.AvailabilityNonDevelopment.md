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
[MarkerFlags](Unity.Profiling.LowLevel.MarkerFlags.html).AvailabilityNonDevelopment

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

Specifies that marker is present in non-development Players.

Use _AvailabilityNonDevelopment_ to determine whether or not a profiler marker
or counter is available in non-development Players.

    
    
    using System.Collections.Generic;
    using Unity.Profiling.LowLevel;
    using Unity.Profiling.LowLevel.Unsafe;  
      
    public class Example
    {
        public static unsafe void WriteAllNonDevelopmentStatsToFile(string filePath)
        {
            using (var writer = new System.IO.StreamWriter(filePath))
            {
                var availableStatHandles = new List<[ProfilerRecorderHandle](Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.html)>();
                [ProfilerRecorderHandle.GetAvailable](Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.GetAvailable.html)(availableStatHandles);
                foreach (var h in availableStatHandles)
                {
                    var statDesc = [ProfilerRecorderHandle.GetDescription](Unity.Profiling.LowLevel.Unsafe.ProfilerRecorderHandle.GetDescription.html)(h);
                    if (!statDesc.Flags.HasFlag([MarkerFlags.AvailabilityNonDevelopment](Unity.Profiling.LowLevel.MarkerFlags.AvailabilityNonDevelopment.html)))
                        continue;  
      
                    var name = System.Text.Encoding.UTF8.GetString(statDesc.NameUtf8, statDesc.NameUtf8Len);
                    writer.WriteLine($"{name};{statDesc.Flags}");
                }
            }
        }
    }
    

Use _AvailabilityNonDevelopment_ to signify that a profiler marker created
with the help of
[ProfilerUnsafeUtility.CreateMarker](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateMarker.html)
is available in non-development Players.

    
    
    using Unity.Collections.LowLevel.Unsafe;
    using Unity.Profiling.LowLevel;
    using Unity.Profiling.LowLevel.Unsafe;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    class Example
    {
        static readonly IntPtr markerHandle = [ProfilerUnsafeUtility.CreateMarker](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CreateMarker.html)("MyMarker", [ProfilerUnsafeUtility.CategoryScripts](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.CategoryScripts.html), [MarkerFlags.AvailabilityNonDevelopment](Unity.Profiling.LowLevel.MarkerFlags.AvailabilityNonDevelopment.html), 0);
        static unsafe void DoWork(int num)
        {
            [ProfilerUnsafeUtility.BeginSample](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.BeginSample.html)(markerHandle);
            //...
            [ProfilerUnsafeUtility.EndSample](Unity.Profiling.LowLevel.Unsafe.ProfilerUnsafeUtility.EndSample.html)(markerHandle);
        }
    }
    

**Note:**  
_AvailabilityNonDevelopment_ flag has no effect on the
[ProfilerMarker](Unity.Profiling.ProfilerMarker.html) creation as
[ProfilerMarker](Unity.Profiling.ProfilerMarker.html) API is Development
Player only.

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

