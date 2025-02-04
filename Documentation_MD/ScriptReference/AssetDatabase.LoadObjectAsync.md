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

#  [AssetDatabase](AssetDatabase.html).LoadObjectAsync

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

public static [AssetDatabaseLoadOperation](AssetDatabaseLoadOperation.html)
LoadObjectAsync(string assetPath, long localId);

### Parameters

assetPath | Path of the asset to load.  
---|---  
localId | The local identifier of the object that you want to load. This allows you to load a specific object and its dependencies as opposed to the entire asset.  
  
### Returns

**AssetDatabaseLoadOperation** A UnityEditor.AssetDatabaseLoadOperation which
you can use to track the progress of the operation.

### Description

Loads a specific Object and its dependencies from an Asset file
asynchronously.

All paths are relative to the project folder, for example:
"Assets/MyTextures/hello.png".  
  
Additional resources:
[AssetDatabase.TryGetGUIDAndLocalFileIdentifier](AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html),
[GlobalObjectId.targetObjectId](GlobalObjectId-targetObjectId.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Collections;  
      
    public class MyPlayer : [MonoBehaviour](MonoBehaviour.html)
    {
        public IEnumerator Start()
        {
            // This will load all objects in the fbx and return a single [Mesh](Mesh.html) object.
            [Mesh](Mesh.html) m = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[Mesh](Mesh.html)>("Assets/test.fbx");  
      
            [AssetDatabase.TryGetGUIDAndLocalFileIdentifier](AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html)(m, out string guid, out long localId);  
      
            // At some point after the [Mesh](Mesh.html) may or may not have unloaded we can reload just the mesh
            [AssetDatabaseLoadOperation](AssetDatabaseLoadOperation.html) op = [AssetDatabase.LoadObjectAsync](AssetDatabase.LoadObjectAsync.html)("Assets/test.fbx", localId);  
      
            // yield until the operation is completed
            while (!op.isDone)
                yield return null;  
      
            [Mesh](Mesh.html) reloadedMesh = ([Mesh](Mesh.html))op.LoadedObject;
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

