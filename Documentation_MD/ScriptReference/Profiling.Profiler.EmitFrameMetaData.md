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

#  [Profiler](Profiling.Profiler.html).EmitFrameMetaData

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

public static void EmitFrameMetaData(Guid id, int tag, Array data);

## Declaration

public static void EmitFrameMetaData(Guid id, int tag, List<T> data);

## Declaration

public static void EmitFrameMetaData(Guid id, int tag, NativeArray<T> data);

### Parameters

id | Module identifier. Used to distinguish metadata streams between different plugins, packages or modules.  
---|---  
tag | Data stream index.  
data | Binary data.  
  
### Description

Write metadata associated with the current frame to the Profiler stream.

Use _EmitFrameMetaData_ to write arbitrary binary data to the profiler stream.
Data must contain only blittable types.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Diagnostics;
    using Unity.Collections;
    using UnityEngine;
    using UnityEngine.Profiling;  
      
    public class Example
    {
        public struct TextureInfo
        {
            public int format;
            public int w;
            public int h;
        }  
      
        public static readonly Guid MyProjectId = new Guid("7E1DEA84-51F1-477A-82B5-B5C57AC1EBF7");
        public static readonly int TextureInfoTag = 0;
        public static readonly int TextureDataTag = 1;  
      
        [Conditional("ENABLE_PROFILER")]
        public void EmitTextureToProfilerStream([Texture2D](Texture2D.html) t)
        {
            if (![Profiler.enabled](Profiling.Profiler-enabled.html))
                return;
            TextureInfo textureInfo = new TextureInfo() { format = (int)t.format, w = t.width, h = t.height };
            NativeArray<byte> textureData = t.GetRawTextureData<byte>();
            [Profiler.EmitFrameMetaData](Profiling.Profiler.EmitFrameMetaData.html)(MyProjectId, TextureInfoTag, new[] { textureInfo });
            [Profiler.EmitFrameMetaData](Profiling.Profiler.EmitFrameMetaData.html)(MyProjectId, TextureDataTag, textureData);
        }
    }
    

**Note:**  
Writing large chunks of data might increase the Profiler's overhead and memory
usage. Always check if Profiler is [enabled](Profiling.Profiler-enabled.html)
before generating data. When possible, write data in small chunks to reduce
memory usage.  
  
Additional resources:
[FrameDataView.GetFrameMetaData](Profiling.FrameDataView.GetFrameMetaData.html).

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

