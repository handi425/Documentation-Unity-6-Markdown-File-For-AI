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

#  [Provider](VersionControl.Provider.html).Resolve

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
Resolve([VersionControl.AssetList](VersionControl.AssetList.html) assets,
[VersionControl.ResolveMethod](VersionControl.ResolveMethod.html)
resolveMethod);

### Parameters

assets | List of assets to resolve.  
---|---  
resolveMethod | How the assets should be resolved.  
  
### Description

Starts a task that will resolve the conflicting assets in version control.

When conflicts between the depot and the local version of the asset appear you
can resolve them by keeping either your own copy or the incoming copy.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    public class EditorScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Version Control/ResolveUseTheirs")]
        public static void ExampleResolve()
        {
            [AssetList](VersionControl.AssetList.html) assets = new [AssetList](VersionControl.AssetList.html)();
            assets.Add([Provider.GetAssetByPath](VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs"));
            [Task](VersionControl.Task.html) t = [Provider.Resolve](VersionControl.Provider.Resolve.html)(assets, [ResolveMethod.UseTheirs](VersionControl.ResolveMethod.UseTheirs.html));
            t.Wait();
        }
    }
    

The code above will resolve the "ExampleAsset.cs" file's conflict by
discarding local changes and only keeping the incoming ones.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    public class EditorScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Version Control/ResolveUseMerged")]
        public static void ExampleResolve()
        {
            [AssetList](VersionControl.AssetList.html) assets = new [AssetList](VersionControl.AssetList.html)();
            assets.Add([Provider.GetAssetByPath](VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs"));
            [Task](VersionControl.Task.html) t1 = [Provider.Merge](VersionControl.Provider.Merge.html)(assets);
            t1.Wait();
            [Task](VersionControl.Task.html) t2 = [Provider.Resolve](VersionControl.Provider.Resolve.html)(assets, [ResolveMethod.UseMerged](VersionControl.ResolveMethod.UseMerged.html));
            t2.Wait();
        }
    }
    

The code above shows a third way of resolving the conflict - merging the two
versions together. The correct way to do this is to first, call the
[Provider.Merge](VersionControl.Provider.Merge.html) task on the conflicting
assets and then resolve them using the
[Provider.Resolve](VersionControl.Provider.Resolve.html) task with the
[ResolveMethod.UseMerged](VersionControl.ResolveMethod.UseMerged.html) method.

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

