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

#  [ArchiveHandle](Unity.IO.Archive.ArchiveHandle.html).Compression

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

public [CompressionType](CompressionType.html) Compression;

### Description

The type of compression the archive uses.

Only accessible if the archive loaded successfully.  
  
Additional resources: [AssetBundles compression](../Manual/AssetBundles-
Cache.html).

    
    
    using Unity.Content;
    using Unity.IO.Archive;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public static class ArchiveUtilities
    {
    #if UNITY_EDITOR
        [[MenuItem](MenuItem.html)("[Debug](Debug.html)/Check Archive Compression")]
        static public void CheckCompression()
        {
            string archivePath = [EditorUtility.OpenFilePanel](EditorUtility.OpenFilePanel.html)("Pick [AssetBundle](AssetBundle.html) or other Unity Archive file", "", "");
            if (archivePath.Length == 0)
                return;  
      
            [Debug.Log](Debug.Log.html)($"[Bundle](Unity.Android.Gradle.Bundle.html) {archivePath} has compression type {GetArchiveCompression(archivePath)}");
        }
    #endif  
      
        static public UnityEngine.CompressionType GetArchiveCompression(string archivePath)
        {
            var archiveHandle = [ArchiveFileInterface.MountAsync](Unity.IO.Archive.ArchiveFileInterface.MountAsync.html)([ContentNamespace.Default](Unity.Content.ContentNamespace.Default.html), archivePath, "temp:");
            archiveHandle.JobHandle.Complete();  
      
            if (archiveHandle.Status == [ArchiveStatus.Failed](Unity.IO.Archive.ArchiveStatus.Failed.html))
                throw new System.ArgumentException($"Failed to load {archivePath}");  
      
            var compression = archiveHandle.Compression;
            archiveHandle.Unmount().Complete();  
      
            return compression;
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

