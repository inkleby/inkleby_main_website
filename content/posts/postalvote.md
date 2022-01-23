Title: Fixing Postal Vote Application
Date: 2016-04-10 12:20
Status: published

I'm currently frantically planning to leave the country for a few months - and I'm unlucky enough to miss several important elections.

I hit the "apply for postal vote" part on the to-leave list and discovered that the postal vote process is still pdf based: you print out the form, fill out the details and have to look up separately the address for which of the 376 addresses you need to send it to. 

Last time I had to do the pdf dance I ended up being the victim of an administrative problem that meant [I didn't get to vote](http://wf-renters.org.uk/2014/09/21/only-56-of-private-renters-are-registered-to-vote/). Since then the registration process has moved online and that sort of thing shouldn't happen - but it stays on your mind.

So I started thinking if there was a way of making this process a little nicer and set it as a one-day project. The end result is [postalvote.inkleby.com](http://postalvote.inkleby.com) - a website that automates some of the fiddlier bits of filling out the form. 

On this page you fill out an electronic version of the form :

* Pre-populates a pdf of the form with your details (which may have been sped up if your browser can autocomplete your address).
* Given the elections you choose, it puts the correct date or date range into the form. 
* Uses your postcode to look up your local authority and gives you the address of the electoral registration office to return the form to. 

You then need to print off the form, sign it, and send it to the address listed. 

This seems like a step in the right direction. If you're like me and your disability means hand-written forms are a bit of a mission this reduces the manual work needed massively. Getting rid of the task of looking up registration offices or election dates reduces friction from the application process - but you still need to have access to a printer, envelope and postage. Can we take out even more steps?

The postal vote is a bit of a dangerous thing, if I know your address and your date of birth (which I do if you're on the open register and your facebook security settings are lax) and am willing to fake your signature, I can not only apply for your postal vote but have it sent to my house. Now this makes it a little obvious when people start investigating  - but the damage is done by then. Keeping it paper based does at least slow you down a bit - and as we'll see the current process is legally required to be paper based. 

This makes me a little anxious about further automating the process of applying for a postal vote. I see two possible ways of going about it - the first is the one-mail approach:

1. You fill out the form
2. Sign online using a widget
3. Micropayment for postage
4. I (or a third-party through some sort of postal api) send the form to the office identified by your postcode. 

This makes me anxious for several reasons. The signature widget technically works, in fact it's already built into the program - you can sign your name using the mouse (or finger on a phone) and it will add the signature into the pdf. But I've turned it off because I think it would be a bad idea to use it. 

One problem is if one of your concerns is accessibility creating a more accessible version of the form only to demand people do a complicated motion with a mouse seems odd. The more substantial problem is the legality of e-signatures. 

In general if all parties agree that an electronic or typed signature is valid then it is as good as a signed signature. In this case signature is required by statute - the Electoral Administration Act 2006 [added the requirements](http://www.legislation.gov.uk/ukpga/2006/22/section/14) for postal vote application to require a signature and date of birth explicitly as an anti-fraud measure. The registration officer is allowed to make exceptions in the case of disability or inability to sign, but there is no reference to alternative means of signing. There's an assumption in the law here that it is the norm to sign in a *"consistent and distinctive way"* - which as more and more voters come of age from an education system that doesn't prioritise penmanship seems unlikely to be true for normal people forever - but the context of this comments make it clear that 'signature' is explicitly referring to a written signature. 

So to enable the easy technical fix of a signature widget you'd first need to check with all 376 electoral registration officers if that's ok - if any say no (and they have reasonable reason not to), you have to add more complicated logic to deal with those councils. If you're anxious about a) taking people's money and not giving them votes or b) [ELECTORAL FRAUD](http://www.legislation.gov.uk/ukpga/2006/22/section/40) you want to be careful here. More so if you're planning on not being in the country while all this is happening.  

But let's leave that hurdle behind and assume it's all alright - your next problem is that you are now the important link in the chain between the voter and their vote. You need to add extra feedback stages (when you send the application off) to reassure people that everything is going ok.  If a hole in your process causes someone not to be able to vote this is quite serious. Is this responsibility something you're happy subcontracting out? I'm not.

So this brings me to the second "two-mail" approach. 

1. You fill out the form. 
2. Micropayment for postage
3. I (or third party) SEND YOU the unsigned form and a pre-paid envelope for the ERO in question. 
4. You sign the form, put it in the envelope and post it. 

This adds time and postage cost to the process but is preferable because a) real signatures b) the voter is the last person to see the form before it is posted - it's their responsibility.

If the current version sees any use I'll give some thought to if it's worth setting up the pipelines for this to work (it is that beautiful thing, a profit-generating piece of civic tech) but then my problem is fleeing the country during EU referendum stage. If I was going to be in the country I would absolutely be buying up envelopes at this point - but if I was I would never have thought to apply for a postal vote in the first place and wouldn't be looking at the problem. Hmm.

Any thoughts? <a href="http://www.twitter.com/alexparsons">@alexparsons</a> or alex (at) inkleby.com