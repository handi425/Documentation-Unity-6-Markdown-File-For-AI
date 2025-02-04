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

# NavMeshBuildSource

struct in UnityEngine.AI

/

Implemented in:[UnityEngine.AIModule](UnityEngine.AIModule.html)

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

The input to the NavMesh builder is a list of NavMesh build sources.

Their shape can be one of the following: mesh, terrain, box, sphere, or
capsule. Each of them is described by a NavMeshBuildSource struct.  
  
You can specify a build source by filling a NavMeshBuildSource struct and
adding that to the list of sources that are passed to the bake function.
Alternatively, you can use the collect API to quickly create NavMesh build
sources from available render meshes or physics colliders. See
[NavMeshBuilder.CollectSources](AI.NavMeshBuilder.CollectSources.html).  
  
If you use this function at runtime, any meshes with read/write access
disabled will not be processed or included in the final NavMesh. See
[Mesh.isReadable](Mesh-isReadable.html).

    
    
    using UnityEngine;
    using UnityEngine.AI;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Make a build source for a box in local space
        public [NavMeshBuildSource](AI.NavMeshBuildSource.html) BoxSource10x10()
        {
            var src = new [NavMeshBuildSource](AI.NavMeshBuildSource.html)();
            src.transform = transform.localToWorldMatrix;
            src.shape = [NavMeshBuildSourceShape.Box](AI.NavMeshBuildSourceShape.Box.html);
            src.size = new [Vector3](Vector3.html)(10.0f, 0.1f, 10.0f);
            return src;
        }
    }
    

### Properties

[area](AI.NavMeshBuildSource-area.html)| Describes the area type of the
NavMesh surface for this object.  
---|---  
[component](AI.NavMeshBuildSource-component.html)| Points to the owning
component - if available, otherwise null.  
[generateLinks](AI.NavMeshBuildSource-generateLinks.html)| Enables the links
generation for this object.  
[shape](AI.NavMeshBuildSource-shape.html)| The type of the shape this source
describes. Additional resources: NavMeshBuildSourceShape.  
[size](AI.NavMeshBuildSource-size.html)| Describes the dimensions of the
shape.  
[sourceObject](AI.NavMeshBuildSource-sourceObject.html)| Describes the object
referenced for Mesh and Terrain types of input sources.  
[transform](AI.NavMeshBuildSource-transform.html)| Describes the local to
world transformation matrix of the build source. That is, position and
orientation and scale of the shape.  
  
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

