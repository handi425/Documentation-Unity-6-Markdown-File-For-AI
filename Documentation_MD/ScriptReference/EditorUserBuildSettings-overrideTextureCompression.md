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
[EditorUserBuildSettings](EditorUserBuildSettings.html).overrideTextureCompression

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

public static
[Build.OverrideTextureCompression](Build.OverrideTextureCompression.html)
overrideTextureCompression;

### Description

The asset importing override of texture compression.

This setting lets you override the texture compression settings that Unity
uses when it imports assets. This is mostly useful for local development, to
speed up texture importing or build target switching.  
  
This setting affects all textures in your project, and overrides the import
settings for individual textures. For example, if a texture's import settings
indicate that a "Normal" compressor quality should be used, but
`overrideTextureCompression` is set to
[OverrideTextureCompression.ForceFastCompressor](Build.OverrideTextureCompression.ForceFastCompressor.html),
the texture will be compressed with "Fast" compressor quality setting.  
  
Overriding the texture compression format can increase the speed of the import
process considerably, but it is important to understand the implications. For
information on the effects of the different values, see the documentation for
the [OverrideTextureCompression](Build.OverrideTextureCompression.html) enum.  
  
The Unity editor command line argument `-overrideTextureCompression` can also
be used to set this.  
  
Additional resources:
[OverrideTextureCompression](Build.OverrideTextureCompression.html),
[EditorUserBuildSettings.overrideMaxTextureSize](EditorUserBuildSettings-
overrideMaxTextureSize.html), [Texture Importer](../Manual/class-
TextureImporter.html), [command line
arguments](../Manual/CommandLineArguments.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Build;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("Example/[Switch](PlayerSettings.Switch.html) textures to import with Fast compressor")]
        public static void OverrideToFastCompressor()
        {
            [EditorUserBuildSettings.overrideTextureCompression](EditorUserBuildSettings-overrideTextureCompression.html) = [OverrideTextureCompression.ForceFastCompressor](Build.OverrideTextureCompression.ForceFastCompressor.html);
            [AssetDatabase.Refresh](AssetDatabase.Refresh.html)();
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

