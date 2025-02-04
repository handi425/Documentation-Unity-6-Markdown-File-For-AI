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

#  [MeshWriteData](UIElements.MeshWriteData.html).SetAllVertices

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

public void SetAllVertices(Vertex[] vertices);

### Parameters

vertices | The array of vertices to copy from. The length of the array must match the allocated vertex count.  
---|---  
  
### Description

Fills the values of the allocated vertices with values copied directly from an
array. When this method is called, it is not possible to use SetNextVertex to
fill the allocated vertices array.

When this method is called, it is not possible to use SetNextVertex to fill
the vertices.  
  

    
    
     public class MyVisualElement : [VisualElement](UIElements.VisualElement.html)
     {
         void MyGenerateVisualContent([MeshGenerationContext](UIElements.MeshGenerationContext.html) mgc)
         {
             var meshWriteData = mgc.Allocate(4, 6);
             // meshWriteData has been allocated with 6 indices for 2 triangles  
      
             // ... set the vertices  
      
             // Set indices for the first triangle
             meshWriteData.SetNextIndex(0);
             meshWriteData.SetNextIndex(1);
             meshWriteData.SetNextIndex(2);  
      
             // Set indices for the second triangle
             meshWriteData.SetNextIndex(2);
             meshWriteData.SetNextIndex(1);
             meshWriteData.SetNextIndex(3);
         }
     }
    

* * *

## Declaration

public void SetAllVertices(NativeSlice<Vertex> vertices);

### Parameters

vertices | The array of vertices to copy from. The length of the array must match the allocated vertex count.  
---|---  
  
### Description

Fills the values of the allocated vertices with values copied directly from an
array. When this method is called, it is not possible to use SetNextVertex to
fill the allocated vertices array.

When this method is called, it is not possible to use SetNextVertex to fill
the vertices.

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

