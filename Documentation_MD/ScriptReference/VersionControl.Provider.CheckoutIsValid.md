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

#  [Provider](VersionControl.Provider.html).CheckoutIsValid

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

public static bool
CheckoutIsValid([VersionControl.AssetList](VersionControl.AssetList.html)
assets);

## Declaration

public static bool
CheckoutIsValid([VersionControl.Asset](VersionControl.Asset.html) asset);

## Declaration

public static bool
CheckoutIsValid([VersionControl.AssetList](VersionControl.AssetList.html)
assets, [VersionControl.CheckoutMode](VersionControl.CheckoutMode.html) mode);

## Declaration

public static bool
CheckoutIsValid([VersionControl.Asset](VersionControl.Asset.html) asset,
[VersionControl.CheckoutMode](VersionControl.CheckoutMode.html) mode);

### Parameters

assets | List of assets.  
---|---  
asset | Single asset.  
mode | Specify to check only asset files, meta files or both.  
  
### Description

Given an asset or a list of assets this function returns true if
[Provider.Checkout](VersionControl.Provider.Checkout.html) is a valid task to
perform on at least one of the given assets.

The [CheckoutMode](VersionControl.CheckoutMode.html) option can be used to
narrow down the asset list to a specific type. For example: to only check
whether meta files can be checked out and to ignore their asset file states,
the [CheckoutMode.Meta](VersionControl.CheckoutMode.Meta.html) must be used.

    
    
    using System.Collections.Generic;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    public class EditorScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Version Control/CheckoutIsValid")]
        public static void ExampleCheckoutIsValid()
        {
            [AssetList](VersionControl.AssetList.html) assets = new [AssetList](VersionControl.AssetList.html)();
            assets.Add([Provider.GetAssetByPath](VersionControl.Provider.GetAssetByPath.html)("Assets/ExampleAsset.cs.meta"));
            [Debug.Log](Debug.Log.html)([Provider.CheckoutIsValid](VersionControl.Provider.CheckoutIsValid.html)(assets, [CheckoutMode.Meta](VersionControl.CheckoutMode.Meta.html)));
        }
    }
    

The code above will check the "ExampleAsset.cs" meta file and return true to
the console if It can be checked out.

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

