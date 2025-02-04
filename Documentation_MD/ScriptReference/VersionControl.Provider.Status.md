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

#  [Provider](VersionControl.Provider.html).Status

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
Status([VersionControl.AssetList](VersionControl.AssetList.html) assets);

## Declaration

public static [VersionControl.Task](VersionControl.Task.html)
Status([VersionControl.Asset](VersionControl.Asset.html) asset);

## Declaration

public static [VersionControl.Task](VersionControl.Task.html)
Status([VersionControl.AssetList](VersionControl.AssetList.html) assets, bool
recursively);

## Declaration

public static [VersionControl.Task](VersionControl.Task.html)
Status([VersionControl.Asset](VersionControl.Asset.html) asset, bool
recursively);

## Declaration

public static [VersionControl.Task](VersionControl.Task.html) Status(string[]
assets);

## Declaration

public static [VersionControl.Task](VersionControl.Task.html) Status(string[]
assets, bool recursively);

## Declaration

public static [VersionControl.Task](VersionControl.Task.html) Status(string
asset);

## Declaration

public static [VersionControl.Task](VersionControl.Task.html) Status(string
asset, bool recursively);

### Parameters

assets | The asset list to fetch state information for.  
---|---  
asset | The asset to fetch state information for.  
recursively | If any assets specified are folders this flag will get status for all descendants of the folder as well.  
  
### Description

Starts a task that will fetch the most recent status about the asset or assets
from the revision control system.

The updated assets can be access through the task's assetList property once it
has completed.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    public class EditorScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Version Control/[Status](Progress.Status.html)")]
        public static void ExampleStatus()
        {
            [AssetList](VersionControl.AssetList.html) assets = new [AssetList](VersionControl.AssetList.html)();
            assets.Add([Provider.GetAssetByPath](VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs"));
            [Task](VersionControl.Task.html) t = [Provider.Status](VersionControl.Provider.Status.html)(assets);
            t.Wait();
            t.assetList.ForEach(asset => [Debug.Log](Debug.Log.html)(asset.name + " " + asset.state.ToString()));
        }
    }
    

The example code above will check the status of the given example asset and
its .meta file and output that information into the console.

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

