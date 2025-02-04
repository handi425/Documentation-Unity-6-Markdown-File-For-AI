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

# RunBeforeAssemblyAttribute Constructor

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

public RunBeforeAssemblyAttribute(string assemblyName);

### Parameters

assemblyName | The name of the assembly that should be called after this callback.  
---|---  
  
### Description

Add this attribute to a callback method to indicate that this callback must be
run before any callbacks that are part of the specified assembly.

To define dependencies for a callback, use the following attributes:

  * [RunAfterClassAttribute](Callbacks.RunAfterClassAttribute.html), [RunBeforeClassAttribute](Callbacks.RunBeforeClassAttribute.html)
  * [RunAfterAssemblyAttribute](Callbacks.RunAfterAssemblyAttribute.html), [RunBeforeAssemblyAttribute](Callbacks.RunBeforeAssemblyAttribute.html)
  * [RunAfterPackageAttribute](Callbacks.RunAfterPackageAttribute.html), [RunBeforePackageAttribute](Callbacks.RunBeforePackageAttribute.html)

When the callback is invoked, Unity generates a dependency graph and uses
topological sorting to ensure that all dependencies are run in sequence based
on their dependencies. If callbacks dependencies are not present in the
project then the instruction will be ignored during the generation of the
dependency graph.  
  
**Note:** Defining callback dependencies is currently only supported by the
[AssetPostprocessor.OnPostprocessAllAssets](AssetPostprocessor.OnPostprocessAllAssets.html)
callback.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Callbacks;
    using UnityEngine;  
      
    // This example shows how to ensure that a callback is called before the Addressables assembly has been called.
    class MyPostprocessor : [AssetPostprocessor](AssetPostprocessor.html)
    {
        [RunBeforeAssembly("Unity.Addressables.Editor")]
        static void OnPostprocessAllAssets(string[] importedAssets, string[] deletedAssets, string[] movedAssets, string[] movedFromAssetPaths)
        {
            [Debug.Log](Debug.Log.html)("MyAllPostprocessor");
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

