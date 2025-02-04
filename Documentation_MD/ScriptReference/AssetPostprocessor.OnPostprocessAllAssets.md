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
[AssetPostprocessor](AssetPostprocessor.html).OnPostprocessAllAssets(string[]
importedAssets, string[] deletedAssets, string[] movedAssets, string[]
movedFromAssetPaths, bool didDomainReload)

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

importedAssets | Array of paths to imported assets.  
---|---  
deletedAssets | Array of paths to deleted assets.  
movedAssets | Array of paths to moved assets.  
movedFromAssetPaths | Array of original paths for moved assets.  
didDomainReload | Boolean set to true if there has been a domain reload.  
  
### Description

This is called after importing of any number of assets is complete (when the
Assets progress bar has reached the end).

This call may occur after a manual reimport, or when you move an asset or a
folder of assets to a new location in the Project window. Every string array
item contains a file path relative to the Assets folder, under the Project
root. `importedAssets` contains paths of all assets used in the operation.
Each consecutive index of `movedAssets` and `movedFromAssetPaths` refers to
the same asset.  
  
If you perform a bulk operation on several individual assets instead of a
folder containing those assets, this function will be called once per asset
with each individual asset as the only item in the various arrays.  
  
OnPostProcessAllAssets is called when the asset database finishes importing
assets. You can safely perform any asset database operations from within this
callback, such as loading, importing, moving or deleting assets.  
  
OnPostProcessAllAssets should be used for initialization after a domain
reload, if the initialization requires asset operations like loading of
assets. `didDomainReload` parameter can be checked whether there has been a
domain reload. All domain reloads will cause OnPostprocessAllAssets to be
called.  
  
Note: If your code causes any new asset imports during this callback,
OnPostProcessAllAssets will be called again once those new imports are
complete.  
  
Note that this function must be declared as `static`, that is it will not be
called correctly if it is declared as an instance function.  
  
The order specified by GetPostprocessOrder does not affect this function,
instead the order can be controlled by defining dependencies using the
following attributes:

  * [RunAfterClassAttribute](Callbacks.RunAfterClassAttribute.html), [RunBeforeClassAttribute](Callbacks.RunBeforeClassAttribute.html)
  * [RunAfterAssemblyAttribute](Callbacks.RunAfterAssemblyAttribute.html), [RunBeforeAssemblyAttribute](Callbacks.RunBeforeAssemblyAttribute.html)
  * [RunAfterPackageAttribute](Callbacks.RunAfterPackageAttribute.html), [RunBeforePackageAttribute](Callbacks.RunBeforePackageAttribute.html)

Note: A version of this callback without the `didDomainReload` parameter is
also available (**OnPostprocessAllAssets(string[] importedAssets, string[]
deletedAssets, string[] movedAssets, string[] movedFromAssetPaths)**)

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    class MyAllPostprocessor : [AssetPostprocessor](AssetPostprocessor.html)
    {
        static void OnPostprocessAllAssets(string[] importedAssets, string[] deletedAssets, string[] movedAssets, string[] movedFromAssetPaths, bool didDomainReload)
        {
            foreach (string str in importedAssets)
            {
                [Debug.Log](Debug.Log.html)("Reimported [Asset](VersionControl.Asset.html): " + str);
            }
            foreach (string str in deletedAssets)
            {
                [Debug.Log](Debug.Log.html)("Deleted [Asset](VersionControl.Asset.html): " + str);
            }  
      
            for (int i = 0; i < movedAssets.Length; i++)
            {
                [Debug.Log](Debug.Log.html)("Moved [Asset](VersionControl.Asset.html): " + movedAssets[i] + " from: " + movedFromAssetPaths[i]);
            }  
      
            if (didDomainReload)
            {
                [Debug.Log](Debug.Log.html)("Domain has been reloaded");
            }
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

