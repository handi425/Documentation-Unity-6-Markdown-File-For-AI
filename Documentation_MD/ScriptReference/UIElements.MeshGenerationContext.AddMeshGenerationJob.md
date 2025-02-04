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
[MeshGenerationContext](UIElements.MeshGenerationContext.html).AddMeshGenerationJob

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

public void
AddMeshGenerationJob([Unity.Jobs.JobHandle](Unity.Jobs.JobHandle.html)
jobHandle);

### Parameters

jobHandle | JobHandle to wait for.  
---|---  
  
### Description

Instructs the renderer to wait for the completion of the provided JobHandle
before beginning processing the meshes.

The following code example shows how to use a job to generate a mesh:

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using Unity.Collections;
    using Unity.Jobs;
    using UnityEngine;
    using UnityEngine.UIElements;  
      
    class CheckerboardElement : [VisualElement](UIElements.VisualElement.html)
    {
        struct CheckerboardJob : [IJob](Unity.Jobs.IJob.html)
        {
            [WriteOnly] public NativeSlice<[Vertex](UIElements.Vertex.html)> vertices;
            [WriteOnly] public NativeSlice<ushort> indices;  
      
            public int horizontalCount;
            public int verticalCount;
            public float divisions;
            public [Color32](Color32.html) color1;
            public [Color32](Color32.html) color2;  
      
            public void Execute()
            {
                Span<[Color32](Color32.html)> colors = stackalloc [Color32](Color32.html)[2];
                colors[0] = color1;
                colors[1] = color2;
                int colorIndex = 0;  
      
                int vCount = 0;
                int iCount = 0;  
      
                float left = 0;
                float right = divisions;
                for (int i = 0; i < horizontalCount; ++i)
                {
                    float top = 0;
                    float bottom = divisions;
                    for (int j = 0; j < verticalCount; ++j)
                    {
                        colorIndex = (i ^ j) & 1;  
      
                        [Color32](Color32.html) color = colors[colorIndex];  
      
                        vertices[vCount + 0] = new [Vertex](UIElements.Vertex.html) { position = new [Vector3](Vector3.html)(left, bottom), tint = color };
                        vertices[vCount + 1] = new [Vertex](UIElements.Vertex.html) { position = new [Vector3](Vector3.html)(left, top), tint = color };
                        vertices[vCount + 2] = new [Vertex](UIElements.Vertex.html) { position = new [Vector3](Vector3.html)(right, top), tint = color };
                        vertices[vCount + 3] = new [Vertex](UIElements.Vertex.html) { position = new [Vector3](Vector3.html)(right, bottom), tint = color };  
      
                        indices[iCount + 0] = (ushort)(vCount + 0);
                        indices[iCount + 1] = (ushort)(vCount + 1);
                        indices[iCount + 2] = (ushort)(vCount + 2);
                        indices[iCount + 3] = (ushort)(vCount + 2);
                        indices[iCount + 4] = (ushort)(vCount + 3);
                        indices[iCount + 5] = (ushort)(vCount + 0);  
      
                        vCount += 4;
                        iCount += 6;
                        top += divisions;
                        bottom += divisions;
                    }  
      
                    left += divisions;
                    right += divisions;
                }
            }
        }  
      
        int m_Divisions;
        [Color32](Color32.html) m_Color1;
        [Color32](Color32.html) m_Color2;  
      
        public CheckerboardElement(int divisions, [Color32](Color32.html) color1, [Color32](Color32.html) color2)
        {
            generateVisualContent = OnGenerateVisualContent;
            m_Divisions = divisions;
            m_Color1 = color1;
            m_Color2 = color2;
        }  
      
        void OnGenerateVisualContent([MeshGenerationContext](UIElements.MeshGenerationContext.html) mgc)
        {
            int horizontalCount = [Mathf.FloorToInt](Mathf.FloorToInt.html)(layout.width / m_Divisions);
            int verticalCount = [Mathf.FloorToInt](Mathf.FloorToInt.html)(layout.height / m_Divisions);  
      
            if (horizontalCount == 0 || verticalCount == 0)
                return;  
      
            var job = new CheckerboardJob
            {
                horizontalCount = horizontalCount,
                verticalCount = verticalCount,
                divisions = m_Divisions,
                color1 = m_Color1,
                color2 = m_Color2
            };  
      
            int quads = horizontalCount * verticalCount;  
      
            mgc.AllocateTempMesh(quads * 4, quads * 6, out job.vertices, out job.indices);
            mgc.DrawMesh(job.vertices, job.indices);  
      
            [JobHandle](Unity.Jobs.JobHandle.html) jobHandle = job.Schedule();
            mgc.AddMeshGenerationJob(jobHandle);
        }
    }
    

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

