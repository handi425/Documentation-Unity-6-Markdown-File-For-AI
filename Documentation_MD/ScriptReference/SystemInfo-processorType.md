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

#  [SystemInfo](SystemInfo.html).processorType

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

public static string processorType;

### Description

Processor name (Read Only).

Will return [SystemInfo.unsupportedIdentifier](SystemInfo-
unsupportedIdentifier.html) on platforms which don't support this property.

    
    
    using UnityEngine;
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Globalization;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Prints using the following format - "Intel(R) Core(TM)2 Quad CPU Q6600 @ 2.40GHz"
            print([SystemInfo.processorType](SystemInfo-processorType.html));  
      
            // Print out the architecture of the running process.
            // We can use the Environment property Is64BitProcess along with [SystemInfo.processorType](SystemInfo-processorType.html) to figure it out.
            // Do a case insensitive string check.
            if (CultureInfo.InvariantCulture.CompareInfo.IndexOf([SystemInfo.processorType](SystemInfo-processorType.html), "ARM", CompareOptions.IgnoreCase) >= 0)
            {
                if (Environment.Is64BitProcess)
                    [Debug.Log](Debug.Log.html)("ARM64");
                else
                    [Debug.Log](Debug.Log.html)("ARM");
            }
            else
            {
                // Must be in the x86 family.
                if (Environment.Is64BitProcess)
                    [Debug.Log](Debug.Log.html)("x86_64");
                else
                    [Debug.Log](Debug.Log.html)("x86");
            }
        }
    }
    

Additional resources: [SystemInfo.processorCount](SystemInfo-
processorCount.html), [SystemInfo.processorFrequency](SystemInfo-
processorFrequency.html). On Android prior to 2019.3 this property would
return the process architecture rather than the CPU name. To determine the
architecture of the running process see the example code.

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

