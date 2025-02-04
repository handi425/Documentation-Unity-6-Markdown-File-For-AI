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

#  [CacheServer](CacheServer.html).UploadArtifacts(GUID[] guids, bool
uploadAllRevisions)

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

### Parameters

guids | Array of GUIDs to upload to the Accelerator. If array is empty, all assets are uploaded.  
---|---  
uploadAllRevisions | Specifies if all revisions of the Assets corresponding to the supplied GUIDs should also be uploaded. Each time an Asset is edited, a new revision is created. Revisions also include non-primary artifacts. That is, artifacts not generated via their default importer for an asset type, but by another importer. One example of this is the Preview importer. That uses the same Asset GUID but a different importer to generate an asset preview.  
  
### Description

Upload the specified GUIDs to the Accelerator. If keys is empty, all assets
are uploaded.

Use this method to upload assets to the Accelerator in an asynchronous way.
This API can be used when an already imported project is opened with Unity but
was not previously imported using the Accelerator. This method allows you to
upload Assets specified by the guids array. If the supplied array is empty or
null, all assets are uploaded. Additionally, the command line argument
-cacheServerUploadExistingImports if you would like to run this on a
Continuous Integration server. **NOTE:** Non-primary artifacts will also be
uploaded when using this API. For example, if you have a Prefab with a
preview, both the Prefab and its Preview will be uploaded to the Accelerator
when specifying only the GUID of the Prefab.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class CacheServerExamples
    {
        [[MenuItem](MenuItem.html)("[CacheServer](CacheServer.html)/UploadAllAssetsToCacheServer")]
        public static void UploadAllAssetsToCacheServer()
        {
            //This will upload all Assets to Accelerator
            [CacheServer.UploadArtifacts](CacheServer.UploadArtifacts.html)();
        }  
      
    }
    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class CacheServerExamples
    {
        [[MenuItem](MenuItem.html)("[CacheServer](CacheServer.html)/UploadAllPrefabsToCacheServer")]
        public static void UploadAllPrefabsToCacheServer()
        {
            var prefabFileGUIDs = [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("t:Prefab");
            var guids = new GUID[prefabFileGUIDs.Length];
            var counter = 0;
            foreach (var curGUID in prefabFileGUIDs)
            {
                guids[counter] = new GUID(curGUID);
                ++counter;
            }  
      
            //This will upload all Prefabs to Accelerator
            [CacheServer.UploadArtifacts](CacheServer.UploadArtifacts.html)(guids);
        }
    }
    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    public class CacheServerExamples
    {
        [[MenuItem](MenuItem.html)("[CacheServer](CacheServer.html)/UploadAllScriptsToCacheServer")]
        public static void UploadAllScriptsToCacheServer()
        {
            var scriptFileGUIDs = [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("t:Script");
            var guids = new GUID[scriptFileGUIDs.Length];
            var counter = 0;
            foreach (var curGUID in scriptFileGUIDs)
            {
                guids[counter] = new GUID(curGUID);
                ++counter;
            }
            //This will upload all Scripts to Accelerator
            [CacheServer.UploadArtifacts](CacheServer.UploadArtifacts.html)(guids);
        }
    }
    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class CacheServerExamples
    {
        [[MenuItem](MenuItem.html)("[CacheServer](CacheServer.html)/UploadAllTextureVersionsToCacheServer")]
        public static void UploadAllTextureVersionsToCacheServer()
        {
            var textureGUIDs = [AssetDatabase.FindAssets](AssetDatabase.FindAssets.html)("t:[Texture](Texture.html)");
            var guids = new GUID[textureGUIDs.Length];
            var counter = 0;
            foreach (var curGUID in textureGUIDs)
            {
                guids[counter] = new GUID(curGUID);
                ++counter;
            }  
      
            //Every time an asset is modified, and imported, a new revision
            //of that [Asset](VersionControl.Asset.html) is created. As such, the history of the import
            //results of an [Asset](VersionControl.Asset.html) are kept around, and purged when the [Editor](Editor.html) 
            //is restarted.
            //Supplying the uploadAllRevisions as true, then all revisions 
            //of an asset will be uploaded.
            [CacheServer.UploadArtifacts](CacheServer.UploadArtifacts.html)(guids, true);
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

