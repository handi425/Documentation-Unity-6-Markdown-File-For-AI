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

# PreferBinarySerialization

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

Prefer ScriptableObject derived type to use binary serialization regardless of
project's asset serialization mode.

This is useful for custom asset types that contain large amounts of data.
Always keeping them stored as binary can both improve read/write performance,
as well as produce more compact representations on disk. The major downsides
are that binary asset files are no longer humanly readable, and that you can
no longer merge them in your revision control software.  
  
Asset serialization in Unity always uses a consistent serialization mode
throughout the entirety of each file. As a result, when an asset file contains
multiple assets, it might not always be possible to respect the desire to
force a specific asset to use binary serialization. The serialization mode of
an asset file is controlled by the main asset at that path. As a result, care
has to be taken when composing complex assets using AssetDabase.CreateAsset
and [AssetDatabase.AddObjectToAsset](AssetDatabase.AddObjectToAsset.html) to
ensure that the main asset is the object with this attribute set. Scene files
always follow the asset serialization mode configured in the project, thus
PreferBinarySerialization is always ignored for assets embedded in Scenes.  
  
The attribute can only be applied to ScriptableObject derived classes, it will
be ignored for all other types.

    
    
    using UnityEngine;  
      
    // Custom asset type that prefers binary serialization.
    //
    // Create a new asset file by going to "[Asset](VersionControl.Asset.html)/Create/Custom [Data](Unity.Android.Gradle.Manifest.Data.html)".
    // If you open this new asset in a text editor, you can see how it
    // is not affected by changing the project asset serialization mode.
    //
    [CreateAssetMenu]
    [[PreferBinarySerialization](PreferBinarySerialization.html)]
    public class CustomData : [ScriptableObject](ScriptableObject.html)
    {
        public float[] lotsOfFloatData = new[] { 1f, 2f, 3f };
        public byte[] lotsOfByteData = new byte[] { 4, 5, 6 };
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

