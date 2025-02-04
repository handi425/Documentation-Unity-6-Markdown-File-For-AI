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

#  [TextureImporter](TextureImporter.html).GetPlatformTextureSettings

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

[Switch to Manual](../Manual/class-TextureImporter.html "Go to TextureImporter
Component in the Manual")

## Declaration

public bool GetPlatformTextureSettings(string platform, out int
maxTextureSize, out [TextureImporterFormat](TextureImporterFormat.html)
textureFormat, out int compressionQuality, out bool etc1AlphaSplitEnabled);

### Parameters

platform | The platform for which settings are required (see options below).  
---|---  
maxTextureSize | Maximum texture width/height in pixels.  
textureFormat | Format of the texture for the given platform.  
compressionQuality | Value from 0..100, equivalent to the standard JPEG quality setting.  
etc1AlphaSplitEnabled | Status of the ETC1 and alpha split flag.  
  
### Returns

**bool** True if the platform override was found, false if no override was
found.

### Description

Gets platform specific texture settings.

The values for the chosen platform are returned in the `out` parameters. The
options for the `platform` string are as follows:

  * Standalone
  * Web
  * iPhone
  * Android
  * Windows Store Apps
  * tvOS

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.UI;
    using System.Collections;  
      
    public class [DisplayInfo](DisplayInfo.html) : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("PlatformSettings/GetSettingsForAndroid")]
        static void GetAndroidSettings()
        {
            string  platformString = "[Android](PlayerSettings.Android.html)";
            int     platformMaxTextureSize = 0;
            [TextureImporterFormat](TextureImporterFormat.html) platformTextureFmt;
            int     platformCompressionQuality = 0;
            bool    platformAllowsAlphaSplit = false;  
      
            [TextureImporter](TextureImporter.html) ti = ([TextureImporter](TextureImporter.html))TextureImporter.GetAtPath("Assets/characters.png");
            if (ti.GetPlatformTextureSettings(platformString, out platformMaxTextureSize, out platformTextureFmt, out platformCompressionQuality, out platformAllowsAlphaSplit))
            {
                [Debug.Log](Debug.Log.html)("Found some overrides for platform: " + platformString);
            }
        }
    }
    

* * *

## Declaration

public bool GetPlatformTextureSettings(string platform, out int
maxTextureSize, out [TextureImporterFormat](TextureImporterFormat.html)
textureFormat, out int compressionQuality);

### Parameters

platform | The platform whose settings are required (see below).  
---|---  
maxTextureSize | Maximum texture width/height in pixels.  
textureFormat | Format of the texture.  
compressionQuality | Value from 0..100, equivalent to the standard JPEG quality setting.  
  
### Returns

**bool** True if the platform override was found, false if no override was
found.

### Description

Gets platform specific texture settings.

The values for the chosen platform are returned in the `out` parameters. The
options for the `platform` string are as follows:

  * Standalone
  * Web
  * iPhone
  * Android
  * Windows Store Apps
  * tvOS

* * *

## Declaration

public bool GetPlatformTextureSettings(string platform, out int
maxTextureSize, out [TextureImporterFormat](TextureImporterFormat.html)
textureFormat);

### Parameters

platform | The platform whose settings are required (see below).  
---|---  
maxTextureSize | Maximum texture width/height in pixels.  
textureFormat | Format of the texture.  
  
### Returns

**bool** True if the platform override was found, false if no override was
found.

### Description

Gets platform specific texture settings.

The values for the chosen platform are returned in the `out` parameters. The
options for the `platform` string are as follows:

  * Standalone
  * Web
  * iPhone
  * Android
  * Windows Store Apps
  * tvOS

* * *

## Declaration

public [TextureImporterPlatformSettings](TextureImporterPlatformSettings.html)
GetPlatformTextureSettings(string platform);

### Parameters

platform | The platform whose settings are required (see below).  
---|---  
  
### Returns

**TextureImporterPlatformSettings** A
[TextureImporterPlatformSettings](TextureImporterPlatformSettings.html)
structure containing the platform parameters.

### Description

Gets platform specific texture settings.

The values for the chosen platform are returned in the `out` parameters. The
options for the `platform` string are as follows:

  * Standalone
  * Web
  * iPhone
  * Android
  * Windows Store Apps
  * tvOS

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

