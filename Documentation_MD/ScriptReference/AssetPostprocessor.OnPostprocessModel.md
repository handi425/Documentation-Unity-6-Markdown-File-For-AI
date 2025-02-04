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
[AssetPostprocessor](AssetPostprocessor.html).OnPostprocessModel(GameObject)

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

Add this function to a subclass to get a notification when a model has
completed importing.

This lets you modify the imported Game Object, Meshes, AnimationClips
referenced by it. Please note that the GameObjects, AnimationClips and Meshes
only exist during the import and will be destroyed immediately afterwards.  
  
This function is called before the final Prefab is created and before it is
written to disk, thus you have full control over the generated game objects
and components.  
  
Any references to game objects or meshes will become invalid after the import
has been completed. Thus it is not possible to create a new Prefab in a
different file from OnPostprocessModel that references meshes in the imported
fbx file.  
  
`root` is the root game object of the imported model.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    // Adds a mesh collider to each game object that contains collider in its name
    public class Example : [AssetPostprocessor](AssetPostprocessor.html)
    {
        void OnPostprocessModel([GameObject](GameObject.html) g)
        {
            Apply(g.transform);
        }  
      
        void Apply([Transform](Transform.html) t)
        {
            if (t.name.ToLower().Contains("collider"))
                t.gameObject.AddComponent<[MeshCollider](MeshCollider.html)>();  
      
            // Recurse
            foreach ([Transform](Transform.html) child in t)
                Apply(child);
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

