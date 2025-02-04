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

#  [Provider](VersionControl.Provider.html).Revert

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

public static [VersionControl.Task](VersionControl.Task.html)
Revert([VersionControl.AssetList](VersionControl.AssetList.html) assets,
[VersionControl.RevertMode](VersionControl.RevertMode.html) mode);

## Declaration

public static [VersionControl.Task](VersionControl.Task.html)
Revert([VersionControl.Asset](VersionControl.Asset.html) asset,
[VersionControl.RevertMode](VersionControl.RevertMode.html) mode);

### Parameters

assets | The list of assets to be reverted.  
---|---  
asset | The asset to be reverted.  
mode | How to revert the assets.  
  
### Description

Reverts the specified assets by undoing any changes done since the last time
you synced.

The last sync time is usually when
[Provider.GetLatest](VersionControl.Provider.GetLatest.html) was last issued
but may differ if an external version control client is used at the same time.  
  
Note that after this operation is completed, Asset Database is not refreshed
automatically. It can be updated by calling
[AssetDatabase.Refresh](AssetDatabase.Refresh.html).

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    public class EditorScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Version Control/Revert")]
        public static void ExampleRevert()
        {
            [AssetList](VersionControl.AssetList.html) assets = new [AssetList](VersionControl.AssetList.html)();
            assets.Add([Provider.GetAssetByPath](VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs"));
            [Task](VersionControl.Task.html) t = [Provider.Revert](VersionControl.Provider.Revert.html)(assets, [RevertMode.Normal](VersionControl.RevertMode.Normal.html));
            t.Wait();
        }
    }
    

[Provider.Revert](VersionControl.Provider.Revert.html) can be used with two
different revert modes - normal and unchanged. The normal revert mode reverts
all of the local changes made while the unchanged mode only reverts files that
haven't been modified yet.

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

