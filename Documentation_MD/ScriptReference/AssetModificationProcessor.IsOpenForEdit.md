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
[AssetModificationProcessor](AssetModificationProcessor.html).IsOpenForEdit(string[],List<string>,StatusQueryOptions)

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

assetOrMetaFilePaths | Paths to Assets or their .meta files, relative to the project folder.  
---|---  
outNotEditablePaths | Destination list of non-editable Asset paths.  
statusQueryOptions | Specifies how Unity should query the version control system. The default value is [StatusQueryOptions.UseCachedIfPossible](StatusQueryOptions.UseCachedIfPossible.html).  
  
### Returns

**void** Returns `true` if all files are editable.

### Description

This is called by Unity when inspecting assets to determine if an editor
should be disabled.

Although this is called by Unity's own systems, you can also call it if you
are implementing your own Editor tools such as a custom version control
integration.  
  
Additional resources:
[AssetDatabase.IsOpenForEdit](AssetDatabase.IsOpenForEdit.html),
[StatusQueryOptions](StatusQueryOptions.html).

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    class CustomAssetModificationProcessor : UnityEditor.AssetModificationProcessor
    {
        static bool IsOpenForEdit(string[] paths, List<string> outNotEditablePaths, [StatusQueryOptions](StatusQueryOptions.html) statusQueryOptions)
        {
            [Debug.Log](Debug.Log.html)("IsOpenForEdit:");
            foreach (var path in paths)
                [Debug.Log](Debug.Log.html)(path);
            return true;
        }
    }
    

* * *

### Parameters

assetOrMetaFilePath | Path to the asset file or its .meta file on disk, relative to project folder.  
---|---  
message | Returns a reason for the asset not being open for edit.  
  
### Returns

**void** True if the asset is considered open for edit by the selected version
control system.

### Description

This is called by Unity when inspecting an asset to determine if an editor
should be disabled.

Although this is called by Unity's own systems, you can also call it if you
are implementing your own Editor tools such as a custom version control
integration. Consider using method overload that accepts an array of file
paths to improve version control system performance.

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

