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

#  [WWWForm](WWWForm.html).data

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

public byte[] data;

### Description

(Read Only) The raw data to pass as the POST request body when sending the
form.

Usually, you just pass the WWWForm object directly to the WWW constructor, but
you will need this variable if you want to change the request headers sent to
the web server.  
  
Additional resources: [headers](WWWForm-headers.html) variable.

    
    
    using UnityEngine;
    using System.Collections;
    using System.Collections.Generic;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        IEnumerator Start()
        {
            [WWWForm](WWWForm.html) form = new [WWWForm](WWWForm.html)();
            form.AddField( "name", "value" );
            Dictionary<string, string> headers = form.headers;
            byte[] rawData = form.data;
            string url = "www.myurl.com";  
      
            // Add a custom header to the request.
            // In this case a basic authentication to access a password protected resource.
            headers["Authorization"] = "Basic " + System.Convert.ToBase64String(
                System.Text.Encoding.ASCII.GetBytes("username:password"));  
      
            // Post a request to an URL with our custom headers
            using (WWW www = new WWW(url, rawData, headers))
            {
                yield return www;
                //.. process results from WWW request here...
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

