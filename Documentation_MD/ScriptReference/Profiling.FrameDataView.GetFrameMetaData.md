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

#  [FrameDataView](Profiling.FrameDataView.html).GetFrameMetaData

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

public NativeArray<T> GetFrameMetaData(Guid id, int tag);

## Declaration

public NativeArray<T> GetFrameMetaData(Guid id, int tag, int index);

### Parameters

id | Project or package identifier.  
---|---  
tag | Data stream index.  
index | Chunk index.  
  
### Returns

**NativeArray <T>** Returns the frame metadata as a NativeArray.

### Description

Retrieves metadata associated with the frame.

Use _GetFrameMetaData_ to retrieve the data that the
[Profiler.EmitFrameMetaData](Profiling.Profiler.EmitFrameMetaData.html) method
wrote to the Profiler stream.  
  
Use _id_ to identify the metadata from your Project or package.  
Use _tag_ to distinguish between different data streams.  
Use _index_ to retrieve separate data chunks for each
[Profiler.EmitFrameMetaData](Profiling.Profiler.EmitFrameMetaData.html) called
in a frame.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using Unity.Collections;
    using UnityEditor.Profiling;
    using UnityEditorInternal;
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
      
        public void EmitTextureToProfilerStream([Texture2D](Texture2D.html) t)
        {
            TextureInfo textureInfo = new TextureInfo() { format = (int)t.format, w = t.width, h = t.height };
            NativeArray<byte> textureData = t.GetRawTextureData<byte>();
            [Profiler.EmitFrameMetaData](Profiling.Profiler.EmitFrameMetaData.html)(MyProjectId, TextureInfoTag, new[] { textureInfo });
            [Profiler.EmitFrameMetaData](Profiling.Profiler.EmitFrameMetaData.html)(MyProjectId, TextureDataTag, textureData);
        }  
      
        public [Texture2D](Texture2D.html) GetTextureFromProfilerStream(int frame)
        {
            using (var frameData = ProfilerDriver.GetHierarchyFrameDataView(frame, 0, [HierarchyFrameDataView.ViewModes.Default](Profiling.HierarchyFrameDataView.ViewModes.Default.html), [HierarchyFrameDataView.columnDontSort](Profiling.HierarchyFrameDataView-columnDontSort.html), false))
            {
                NativeArray<TextureInfo> textureInfos = frameData.GetFrameMetaData<TextureInfo>(MyProjectId, TextureInfoTag);
                if (textureInfos.Length == 0)
                    return null;  
      
                NativeArray<byte> textureData = frameData.GetFrameMetaData<byte>(MyProjectId, TextureDataTag);
                if (textureData.Length == 0)
                    return null;  
      
                TextureInfo textureInfo = textureInfos[0];
                [Texture2D](Texture2D.html) texture = new [Texture2D](Texture2D.html)(textureInfo.w, textureInfo.h, ([TextureFormat](TextureFormat.html))textureInfo.format, false);
                texture.LoadRawTextureData(textureData);  
      
                return texture;
            }
        }
    }
    

**Note:**  
The _FrameDataView_ instance defines the lifetime of the returned
''NativeArray'. As such, if _FrameDataView_ is disposed, all returned metadata
becomes invalid and cannot be used. Copy data to a new _NativeArray_ if you
need it for longer duration.  
  
Additional resources:
[Profiler.EmitFrameMetaData](Profiling.Profiler.EmitFrameMetaData.html).

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

