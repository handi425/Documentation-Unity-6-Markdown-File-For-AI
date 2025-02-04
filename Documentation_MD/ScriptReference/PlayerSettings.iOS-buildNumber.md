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

#  [PlayerSettings.iOS](PlayerSettings.iOS.html).buildNumber

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

[Switch to Manual](../Manual/class-PlayerSettings.html "Go to PlayerSettings
Component in the Manual")

public static string buildNumber;

### Description

The build number of the bundle

It is saved to the 'CFBundleVersion' field in the built app's info.plist file.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class BuildNumberExample
    {
        // This example will create a [Menu](Menu.html) [Item](Progress.Item.html) called "Increase Minor Build Number" under "Examples" submenu which when pressed will get the current "Build" property and increase the Minor version by 1 
        // Assuming the "Build" property follows the format Major.Minor.Patch (for example 2.0.5 will be increased to 2.1.0),
        [[MenuItem](MenuItem.html)("Examples/Increase Minor Build Number")]
        public static void IncreaseMinorBuildNumber()
        {
            // Get the current build number value
            string currentBuildNumberString = [PlayerSettings.iOS.buildNumber](PlayerSettings.iOS-buildNumber.html);  
      
            // Separate the build number string to Major, Minor and Patch numbers
            string[] separatedBuildNumbers = currentBuildNumberString.Split('.');  
      
            // Parse the Major and Minor version numbers to integer values
            int majorVersionNumber = int.Parse(separatedBuildNumbers[0]);
            int minorVersionNumber = int.Parse(separatedBuildNumbers[1]);  
      
            // Increment the Minor version number
            minorVersionNumber++;
            
            // [Update](PlayerLoop.Update.html) the buildNumber property with the new values:
            // - keep the old Major version number;
            // - update Minor version number;
            // - replace Patch version number with 0, since Minor version was updated. 
            [PlayerSettings.iOS.buildNumber](PlayerSettings.iOS-buildNumber.html) = string.Format("{0}.{1}.{2}", majorVersionNumber, minorVersionNumber, 0);
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

