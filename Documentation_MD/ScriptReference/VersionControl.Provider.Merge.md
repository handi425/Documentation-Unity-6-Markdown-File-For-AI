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

#  [Provider](VersionControl.Provider.html).Merge

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
Merge([VersionControl.AssetList](VersionControl.AssetList.html) assets);

### Parameters

assets | The list of conflicting assets to be merged.  
---|---  
  
### Description

Initiates a merge task to handle the merging of conflicting Assets. This
invokes a merge tool, which you can set in the External Tools section of the
Preferences window, on the conflicting Assets. When the merge task finishes,
the [AssetList](VersionControl.AssetList.html) only contains the Assets that
the tool could merge.

To correctly resolve the resulting [AssetList](VersionControl.AssetList.html)
states (and replace the files with the correct, merged version), you must call
a subsequent [Provider.Resolve](VersionControl.Provider.Resolve.html) task
with a [ResolveMethod.UseMerged](VersionControl.ResolveMethod.UseMerged.html)
ResolveMethod.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    public class EditorScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Version Control/Merge")]
        public static void ExampleMerge()
        {
            [AssetList](VersionControl.AssetList.html) assets = new [AssetList](VersionControl.AssetList.html)();
            assets.Add([Provider.GetAssetByPath](VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs"));
            [Task](VersionControl.Task.html) t1 = [Provider.Merge](VersionControl.Provider.Merge.html)(assets);
            t1.Wait();
            [Task](VersionControl.Task.html) t2 = [Provider.Resolve](VersionControl.Provider.Resolve.html)(assets, [ResolveMethod.UseMerged](VersionControl.ResolveMethod.UseMerged.html));
            t2.Wait();
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

